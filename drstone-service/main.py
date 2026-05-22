# ============================================================
#  DR. STONE SERVICE – Backend Python
#  Stack: FastAPI + Motor (MongoDB async) + Uvicorn
#  Base de datos: MongoDB Atlas (gratis)
#  Deploy: Render
#
#  Instalar dependencias:
#    pip install fastapi uvicorn motor python-dotenv
# ============================================================

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import Optional
import os

# ── Configuración ─────────────────────────────────────────
MONGO_URI    = os.getenv("MONGO_URI", "mongodb+srv://manu83535_db_user:d68gS8saxYY0l5Kw@cluster0.fyocm6u.mongodb.net/?appName=Cluster0")
DB_NAME      = "drstone_db"
COLLECTION   = "personajes"

# ── App FastAPI ───────────────────────────────────────────
app = FastAPI(
    title       = "Dr. Stone Service API",
    description = "Microservicio REST para personajes de Dr. Stone – FastAPI + MongoDB",
    version     = "1.0.0"
)

# ── CORS (permite peticiones desde GitHub Pages) ──────────
app.add_middleware(
    CORSMiddleware,
    allow_origins     = ["*"],
    allow_methods     = ["GET", "OPTIONS"],
    allow_headers     = ["*"],
)

# ── Conexión MongoDB ──────────────────────────────────────
client     = AsyncIOMotorClient(MONGO_URI)
db         = client[DB_NAME]
collection = db[COLLECTION]

# ── Modelo de respuesta ───────────────────────────────────
class Personaje(BaseModel):
    nombre    : str
    altura    : str
    peso      : str
    reino     : str   # Reino de piedra, Imperio de Tsukasa, etc.
    habilidad : str   # Habilidad principal
    ci        : str   # Coeficiente intelectual o descripción de inteligencia
    imagen    : str

# ── Endpoints ─────────────────────────────────────────────

@app.get("/", tags=["Sistema"])
async def health_check():
    """Verifica que el servidor esté activo."""
    return {
        "message" : "🚀 Dr. Stone Service en línea",
        "version" : "1.0.0 – FastAPI + MongoDB"
    }

@app.get("/personaje/{nombre}", response_model=Personaje, tags=["Dr. Stone"])
async def get_personaje(nombre: str):
    """
    Consulta un personaje de Dr. Stone por nombre.
    El nombre es insensible a mayúsculas (ej: 'senku' o 'Senku').
    """
    # Búsqueda case-insensitive con regex de MongoDB
    personaje = await collection.find_one(
        {"nombre": {"$regex": f"^{nombre.strip()}$", "$options": "i"}},
        {"_id": 0}   # Excluir el _id de MongoDB de la respuesta
    )

    if not personaje:
        raise HTTPException(
            status_code = 404,
            detail      = f"Personaje \"{nombre.lower()}\" no encontrado"
        )

    return personaje