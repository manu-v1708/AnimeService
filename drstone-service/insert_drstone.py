# ============================================================
#  DR. STONE – Script para insertar personajes en MongoDB Atlas
#  Ejecutar UNA SOLA VEZ desde tu computador:
#    python insert_drstone.py
# ============================================================

from pymongo import MongoClient

# ── URI de MongoDB Atlas ──────────────────────────────────
MONGO_URI = "mongodb+srv://manu83535_db_user:d68gS8saxYY0l5Kw@cluster0.fyocm6u.mongodb.net/?appName=Cluster0"

client     = MongoClient(MONGO_URI)
db         = client["drstone_db"]
collection = db["personajes"]

# Borrar datos anteriores si los hay
collection.delete_many({})

personajes = [
    {
        "nombre"    : "senku ishigami",
        "altura"    : "1.80 m",
        "peso"      : "63 kg",
        "reino"     : "Reino de Piedra",
        "habilidad" : "Ciencia y tecnología extrema",
        "ci"        : "CI estimado: 200+ – Genio científico polímata",
        "imagen"    : "https://static.wikia.nocookie.net/dr-stone/images/5/5d/Senku_anime_profile.png"
    },
    {
        "nombre"    : "taiju oki",
        "altura"    : "1.98 m",
        "peso"      : "108 kg",
        "reino"     : "Reino de Piedra",
        "habilidad" : "Fuerza y resistencia física sobrehumana",
        "ci"        : "CI estimado: 80 – Fuerza bruta incomparable",
        "imagen"    : "https://static.wikia.nocookie.net/dr-stone/images/1/1c/Taiju_anime_profile.png"
    },
    {
        "nombre"    : "tsukasa shishio",
        "altura"    : "1.93 m",
        "peso"      : "93 kg",
        "reino"     : "Imperio de Tsukasa",
        "habilidad" : "Combate cuerpo a cuerpo – el humano más fuerte del mundo primitivo",
        "ci"        : "CI estimado: 140 – Estratega y luchador élite",
        "imagen"    : "https://static.wikia.nocookie.net/dr-stone/images/4/4b/Tsukasa_anime_profile.png"
    },
    {
        "nombre"    : "yuzuriha ogawa",
        "altura"    : "1.60 m",
        "peso"      : "48 kg",
        "reino"     : "Reino de Piedra",
        "habilidad" : "Costura y artesanía de precisión",
        "ci"        : "CI estimado: 115 – Habilidad manual excepcional",
        "imagen"    : "https://static.wikia.nocookie.net/dr-stone/images/6/6e/Yuzuriha_anime_profile.png"
    },
    {
        "nombre"    : "chrome",
        "altura"    : "1.68 m",
        "peso"      : "58 kg",
        "reino"     : "Reino de Piedra",
        "habilidad" : "Recolección de minerales y química primitiva",
        "ci"        : "CI estimado: 130 – Científico autodidacta de la era primitiva",
        "imagen"    : "https://static.wikia.nocookie.net/dr-stone/images/3/38/Chrome_anime_profile.png"
    },
    {
        "nombre"    : "kohaku",
        "altura"    : "1.58 m",
        "peso"      : "46 kg",
        "reino"     : "Reino de Piedra",
        "habilidad" : "Combate y sigilo – guerrera élite",
        "ci"        : "CI estimado: 110 – Cazadora y combatiente nata",
        "imagen"    : "https://static.wikia.nocookie.net/dr-stone/images/7/7e/Kohaku_anime_profile.png"
    },
    {
        "nombre"    : "gen asagiri",
        "altura"    : "1.75 m",
        "peso"      : "60 kg",
        "reino"     : "Reino de Piedra",
        "habilidad" : "Mentalismo, manipulación psicológica y engaño",
        "ci"        : "CI estimado: 155 – Maestro de la persuasión y el engaño",
        "imagen"    : "https://static.wikia.nocookie.net/dr-stone/images/8/8c/Gen_anime_profile.png"
    },
    {
        "nombre"    : "ryusui nanami",
        "altura"    : "1.85 m",
        "peso"      : "80 kg",
        "reino"     : "Reino de Piedra",
        "habilidad" : "Navegación y pilotaje de cualquier vehículo",
        "ci"        : "CI estimado: 145 – Multimillonario y navegante experto",
        "imagen"    : "https://static.wikia.nocookie.net/dr-stone/images/d/d5/Ryusui_anime_profile.png"
    },
    {
        "nombre"    : "francois",
        "altura"    : "1.70 m",
        "peso"      : "57 kg",
        "reino"     : "Reino de Piedra",
        "habilidad" : "Chef y mayordomo de habilidades perfectas",
        "ci"        : "CI estimado: 135 – Perfeccionista en todas las artes del servicio",
        "imagen"    : "https://static.wikia.nocookie.net/dr-stone/images/f/f5/Francois_anime_profile.png"
    },
    {
        "nombre"    : "suika",
        "altura"    : "1.35 m",
        "peso"      : "30 kg",
        "reino"     : "Reino de Piedra",
        "habilidad" : "Espionaje, sigilo y exploración",
        "ci"        : "CI estimado: 120 – Espía e investigadora excepcional",
        "imagen"    : "https://static.wikia.nocookie.net/dr-stone/images/9/9e/Suika_anime_profile.png"
    }
]

result = collection.insert_many(personajes)
print(f"✅ {len(result.inserted_ids)} personajes insertados correctamente en MongoDB Atlas")
client.close()