"""Conexión a PostgreSQL."""

import os
from contextlib import contextmanager

import psycopg2
from psycopg2.extras import RealDictCursor


def get_database_url() -> str:
    url = os.environ.get("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL no está configurada.")
    return url


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
