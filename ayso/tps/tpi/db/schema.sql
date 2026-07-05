CREATE TABLE IF NOT EXISTS consultas (
    id SERIAL PRIMARY KEY,
    hostname TEXT NOT NULL,
    memoria_total_kb BIGINT NOT NULL,
    memoria_libre_kb BIGINT NOT NULL,
    procesos_activos INTEGER NOT NULL,
    registrado_en TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
