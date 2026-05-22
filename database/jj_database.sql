-- ============================================================
--  JUJUTSU KAISEN – Base de datos PostgreSQL en Supabase
--  Ejecutar en el SQL Editor de Supabase
-- ============================================================

-- 1. Crear tabla
CREATE TABLE IF NOT EXISTS jjk_personajes (
  id          BIGINT        GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  nombre      VARCHAR(100)  NOT NULL UNIQUE,
  altura      VARCHAR(20)   NOT NULL,
  peso        VARCHAR(20)   NOT NULL,
  grado       VARCHAR(50)   NOT NULL,   -- Grado de hechicero (1, 2, especial...)
  tecnica     VARCHAR(100)  NOT NULL,   -- Técnica maldita principal
  clan        VARCHAR(100)  NOT NULL,   -- Clan o afiliación
  imagen      VARCHAR(255)  NOT NULL    -- URL imagen
);

-- 2. Permisos para que la API pueda leerla
ALTER TABLE jjk_personajes ENABLE ROW LEVEL SECURITY;

CREATE POLICY "lectura_publica_jjk" ON jjk_personajes
AS PERMISSIVE FOR SELECT
USING (true);

GRANT USAGE ON SCHEMA public TO anon;
GRANT USAGE ON SCHEMA public TO authenticated;
GRANT SELECT ON jjk_personajes TO anon;
GRANT SELECT ON jjk_personajes TO authenticated;

-- 3. Insertar 10 personajes
INSERT INTO jjk_personajes (nombre, altura, peso, grado, tecnica, clan, imagen) VALUES

('yuji itadori',
 '1.73 m', '80 kg',
 'Grado Especial (Sukuna)',
 'Divergent Fist / Black Flash',
 'Sin clan (huésped de Ryomen Sukuna)',
 'https://static.wikia.nocookie.net/jujutsu-kaisen/images/c/c5/Yuji_Itadori_anime_profile.png'),

('megumi fushiguro',
 '1.75 m', '70 kg',
 'Grado 2 → Grado 1',
 'Ten Shadows Technique',
 'Clan Zenin (adoptado)',
 'https://static.wikia.nocookie.net/jujutsu-kaisen/images/4/43/Megumi_Fushiguro_anime_profile.png'),

('nobara kugisaki',
 '1.60 m', '50 kg',
 'Grado 3 → Grado 1',
 'Straw Doll Technique',
 'Sin clan',
 'https://static.wikia.nocookie.net/jujutsu-kaisen/images/5/5e/Nobara_Kugisaki_anime_profile.png'),

('satoru gojo',
 '1.90 m', '82 kg',
 'Grado Especial',
 'Infinity / Six Eyes',
 'Clan Gojo',
 'https://static.wikia.nocookie.net/jujutsu-kaisen/images/4/4a/Satoru_Gojo_anime_profile.png'),

('ryomen sukuna',
 '1.87 m', '95 kg',
 'Grado Especial (Rey de las maldiciones)',
 'Cleave / Dismantle / Shrine',
 'Sin clan (antiguo hechicero)',
 'https://static.wikia.nocookie.net/jujutsu-kaisen/images/a/a4/Ryomen_Sukuna_anime_profile.png'),

('aoi todo',
 '1.90 m', '97 kg',
 'Grado 1',
 'Boogie Woogie',
 'Sin clan',
 'https://static.wikia.nocookie.net/jujutsu-kaisen/images/6/6d/Aoi_Todo_anime_profile.png'),

('nanami kento',
 '1.84 m', '83 kg',
 'Grado 1',
 'Ratio Technique',
 'Sin clan',
 'https://static.wikia.nocookie.net/jujutsu-kaisen/images/3/35/Kento_Nanami_anime_profile.png'),

('toge inumaki',
 '1.64 m', '55 kg',
 'Semi-Grado 1',
 'Cursed Speech',
 'Clan Inumaki',
 'https://static.wikia.nocookie.net/jujutsu-kaisen/images/e/e5/Toge_Inumaki_anime_profile.png'),

('suguru geto',
 '1.85 m', '76 kg',
 'Grado Especial',
 'Cursed Spirit Manipulation',
 'Sin clan (expulsado)',
 'https://static.wikia.nocookie.net/jujutsu-kaisen/images/7/74/Suguru_Geto_anime_profile.png'),

('yuta okkotsu',
 '1.78 m', '71 kg',
 'Grado Especial',
 'Copy / Rika (espíritu maldito)',
 'Clan Gojo (descendiente lejano)',
 'https://static.wikia.nocookie.net/jujutsu-kaisen/images/3/3c/Yuta_Okkotsu_anime_profile.png');