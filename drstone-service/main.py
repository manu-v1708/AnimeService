# ============================================================
#  DR. STONE SERVICE – Backend Python
#  Stack: FastAPI + Motor (MongoDB async) + Uvicorn
# ============================================================

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
import os

# ── Configuración ─────────────────────────────────────────
MONGO_URI  = os.getenv("MONGO_URI", "mongodb+srv://manu83535_db_user:d68gS8saxYY0l5Kw@cluster0.fyocm6u.mongodb.net/?appName=Cluster0")
DB_NAME    = "drstone_db"
COLLECTION = "personajes"

# ── App FastAPI ───────────────────────────────────────────
app = FastAPI(
    title       = "Dr. Stone Service API",
    description = "Microservicio REST – FastAPI + MongoDB Atlas",
    version     = "1.0.0"
)

# ── CORS ──────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins  = ["*"],
    allow_methods  = ["GET", "OPTIONS"],
    allow_headers  = ["*"],
)

# ── Conexión MongoDB ──────────────────────────────────────
client     = None
collection = None

@app.on_event("startup")
async def startup_db():
    global client, collection
    try:
        client     = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=10000)
        db         = client[DB_NAME]
        collection = db[COLLECTION]
        # Verificar conexión
        await client.admin.command('ping')
        print("✅ Conectado a MongoDB Atlas")
    except Exception as e:
        print(f"❌ Error conectando a MongoDB: {e}")

@app.on_event("shutdown")
async def shutdown_db():
    global client
    if client:
        client.close()

# ── Modelo ────────────────────────────────────────────────
class Personaje(BaseModel):
    nombre   : str
    altura   : str
    peso     : str
    reino    : str
    habilidad: str
    ci       : str
    imagen   : str

# ── Endpoints ─────────────────────────────────────────────

@app.get("/", tags=["Sistema"])
async def health_check():
    return {
        "message": "🚀 Dr. Stone Service en línea",
        "version": "1.0.0 – FastAPI + MongoDB"
    }

@app.get("/personaje/{nombre}", tags=["Dr. Stone"])
async def get_personaje(nombre: str):
    if collection is None:
        raise HTTPException(status_code=503, detail="Base de datos no disponible")

    personaje = await collection.find_one(
        {"nombre": {"$regex": f"^{nombre.strip()}$", "$options": "i"}},
        {"_id": 0}
    )

    if not personaje:
        raise HTTPException(
            status_code=404,
            detail=f"Personaje \"{nombre.lower()}\" no encontrado"
        )

    return personaje