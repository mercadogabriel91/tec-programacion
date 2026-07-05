import os
import socket
from contextlib import contextmanager

import psycopg2
from psycopg2.extras import RealDictCursor


def get_database_url() -> str:
    user = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASSWORD"]
    host = os.environ.get("POSTGRES_HOST", "db")
    port = os.environ.get("POSTGRES_PORT", "5432")
    dbname = os.environ["POSTGRES_DB"]
    return f"postgresql://{user}:{password}@{host}:{port}/{dbname}"


@contextmanager
def get_connection():
    conn = psycopg2.connect(get_database_url(), cursor_factory=RealDictCursor)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def guardar_consulta(hostname: str, memoria_total_kb: int, memoria_libre_kb: int, procesos_activos: int) -> int:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO consultas (hostname, memoria_total_kb, memoria_libre_kb, procesos_activos)
                VALUES (%s, %s, %s, %s)
                RETURNING id
                """,
                (hostname, memoria_total_kb, memoria_libre_kb, procesos_activos),
            )
            row = cur.fetchone()
            return int(row["id"])


def listar_consultas(limit: int = 10) -> list[dict]:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, hostname, memoria_total_kb, memoria_libre_kb, procesos_activos, registrado_en
                FROM consultas
                ORDER BY registrado_en DESC
                LIMIT %s
                """,
                (limit,),
            )
            return [dict(row) for row in cur.fetchall()]


def verificar_conexion_db() -> bool:
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                cur.fetchone()
        return True
    except Exception:
        return False
