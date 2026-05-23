from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI  = os.getenv("MONGO_URI", "mongodb+srv://manu83535_db_user:d68gS8saxYY0l5Kw@cluster0.fyocm6u.mongodb.net/?appName=Cluster0")
DB_NAME    = "drstone_db"
COLLECTION = "personajes"

# ── Nuevo patrón lifespan (reemplaza on_event) ────────────
db_state = {"client": None, "collection": None}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    try:
        client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=10000)
        await client.admin.command("ping")
        db_state["client"]     = client
        db_state["collection"] = client[DB_NAME][COLLECTION]
        print("✅ Conectado a MongoDB Atlas")
    except Exception as e:
        print(f"❌ Error conectando a MongoDB: {e}")
    
    yield  # La app corre aquí
    
    # Shutdown
    if db_state["client"]:
        db_state["client"].close()

app = FastAPI(
    title       = "Dr. Stone Service API",
    description = "Microservicio REST – FastAPI + MongoDB Atlas",
    version     = "1.0.0",
    lifespan    = lifespan   # 👈 clave
)

app.add_middleware(
    CORSMiddleware,
    allow_origins     = ["*"],
    allow_credentials = False,
    allow_methods     = ["GET", "OPTIONS", "POST"],
    allow_headers     = ["*"],
)

@app.get("/", tags=["Sistema"])
async def health_check():
    return {"message": "🚀 Dr. Stone Service en línea", "version": "1.0.0"}

@app.get("/personaje/{nombre}", tags=["Dr. Stone"])
async def get_personaje(nombre: str):
    collection = db_state["collection"]
    if collection is None:
        raise HTTPException(status_code=503, detail="Base de datos no disponible")

    personaje = await collection.find_one(
        {"nombre": {"$regex": f"^{nombre.strip()}$", "$options": "i"}},
        {"_id": 0}
    )
    if not personaje:
        raise HTTPException(status_code=404, detail=f'Personaje "{nombre}" no encontrado')

    return personaje