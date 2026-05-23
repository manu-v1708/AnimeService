from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import Optional
import os

MONGO_URI  = os.getenv("MONGO_URI", "mongodb+srv://manu83535_db_user:d68gS8saxYY0l5Kw@cluster0.fyocm6u.mongodb.net/?appName=Cluster0")
DB_NAME    = "drstone_db"
COLLECTION = "personajes"

db_state = {"client": None, "collection": None}

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=10000)
        await client.admin.command("ping")
        db_state["client"]     = client
        db_state["collection"] = client[DB_NAME][COLLECTION]
        print("✅ Conectado a MongoDB Atlas")
    except Exception as e:
        print(f"❌ Error conectando a MongoDB: {e}")
    yield
    if db_state["client"]:
        db_state["client"].close()

# ── Modelo de respuesta ───────────────────────────────────
class Personaje(BaseModel):
    nombre   : str
    altura   : str
    peso     : str
    reino    : str
    habilidad: str
    ci       : str
    imagen   : str

class ErrorResponse(BaseModel):
    detail: str

# ── App con metadata para Swagger ────────────────────────
app = FastAPI(
    title          = "Dr. Stone Service API",
    description    = """
## Microservicio REST – Dr. Stone

Consulta personajes del anime **Dr. Stone** almacenados en MongoDB Atlas.

### Personajes disponibles
`senku ishigami` · `taiju oki` · `tsukasa shishio` · `yuzuriha ogawa`
`chrome` · `kohaku` · `gen asagiri` · `ryusui nanami` · `francois` · `suika`
    """,
    version        = "1.0.0",
    lifespan       = lifespan,
    servers        = [{"url": "https://drstone-service.onrender.com", "description": "Producción (Render)"}],
    docs_url       = "/docs",
    redoc_url      = "/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins     = ["*"],
    allow_credentials = False,
    allow_methods     = ["GET", "OPTIONS", "POST"],
    allow_headers     = ["*"],
)

@app.get(
    "/",
    tags    = ["Sistema"],
    summary = "Health-check",
    description = "Verifica que el servidor esté activo"
)
async def health_check():
    return {"message": "🚀 Dr. Stone Service en línea", "version": "1.0.0"}


@app.get(
    "/personaje/{nombre}",
    tags        = ["Dr. Stone"],
    summary     = "Consultar personaje por nombre",
    description = "Devuelve los datos completos de un personaje de Dr. Stone. El nombre no distingue mayúsculas.",
    response_model = Personaje,
    responses   = {
        200: {"description": "Personaje encontrado", "model": Personaje},
        404: {"description": "Personaje no encontrado", "model": ErrorResponse},
        503: {"description": "Base de datos no disponible", "model": ErrorResponse}
    }
)
async def get_personaje(
    nombre: str = None
):
    """
    Busca un personaje por nombre exacto (insensible a mayúsculas).

    **Ejemplos:** `senku ishigami`, `kohaku`, `chrome`
    """
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