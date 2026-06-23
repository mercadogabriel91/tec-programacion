"""Consultas y operaciones de persistencia."""

from __future__ import annotations

import json
from datetime import date, datetime
from typing import Any
from uuid import UUID

from bot.db.connection import get_connection


def get_employee_by_legajo(legajo: str) -> dict[str, Any] | None:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, legajo, full_name, department, vacation_balance
                FROM employees
                WHERE legajo = %s
                """,
                (legajo.strip(),),
            )
            row = cur.fetchone()
            return dict(row) if row else None


def get_employee_requests(employee_id: int) -> list[dict[str, Any]]:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, start_date, end_date, days_requested, status, created_at
                FROM vacation_requests
                WHERE employee_id = %s
                ORDER BY created_at DESC
                LIMIT 5
                """,
                (employee_id,),
            )
            return [dict(row) for row in cur.fetchall()]


def create_vacation_request(
    employee_id: int,
    start_date: date,
    end_date: date,
    days_requested: int,
    reason: str,
    status: str,
) -> dict[str, Any]:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO vacation_requests
                    (employee_id, start_date, end_date, days_requested, reason, status)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id, start_date, end_date, days_requested, status, created_at
                """,
                (employee_id, start_date, end_date, days_requested, reason, status),
            )
            request = dict(cur.fetchone())

            cur.execute(
                """
                UPDATE employees
                SET vacation_balance = vacation_balance - %s
                WHERE id = %s AND vacation_balance >= %s
                RETURNING vacation_balance
                """,
                (days_requested, employee_id, days_requested),
            )
            balance_row = cur.fetchone()
            if not balance_row:
                raise ValueError("Saldo insuficiente al confirmar la solicitud.")

            request["remaining_balance"] = balance_row["vacation_balance"]
            return request


def save_session(
    session_id: UUID,
    state: str,
    employee_id: int | None,
    context: dict[str, Any],
) -> None:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO conversation_sessions (session_id, employee_id, current_state, context, updated_at)
                VALUES (%s, %s, %s, %s::jsonb, %s)
                ON CONFLICT (session_id) DO UPDATE SET
                    employee_id = EXCLUDED.employee_id,
                    current_state = EXCLUDED.current_state,
                    context = EXCLUDED.context,
                    updated_at = EXCLUDED.updated_at
                """,
                (
                    str(session_id),
                    employee_id,
                    state,
                    json.dumps(context, default=str),
                    datetime.utcnow(),
                ),
            )


def load_session(session_id: UUID) -> dict[str, Any] | None:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT session_id, employee_id, current_state, context, updated_at
                FROM conversation_sessions
                WHERE session_id = %s
                """,
                (str(session_id),),
            )
            row = cur.fetchone()
            if not row:
                return None
            data = dict(row)
            if isinstance(data["context"], str):
                data["context"] = json.loads(data["context"])
            return data
