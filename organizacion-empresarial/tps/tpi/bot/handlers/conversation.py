"""Máquina de estados: traduce el diagrama BPMN a lógica conversacional."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from datetime import date
from typing import Any
from uuid import UUID, uuid4

from bot.db import queries
from bot.states import DATE_FORMAT_HINT, GLOBAL_COMMANDS, State
from bot.validators import business_days_between, parse_date, validate_date_range


AUTO_APPROVE_THRESHOLD = int(os.environ.get("AUTO_APPROVE_THRESHOLD", "5"))


@dataclass
class Session:
    session_id: UUID = field(default_factory=uuid4)
    state: State = State.MENU
    employee: dict[str, Any] | None = None
    context: dict[str, Any] = field(default_factory=dict)

    def persist(self) -> None:
        queries.save_session(
            self.session_id,
            self.state.value,
            self.employee["id"] if self.employee else None,
            self.context,
        )


def _help_text() -> str:
    return (
        "Comandos disponibles en cualquier momento:\n"
        "  • menu     — volver al menú principal\n"
        "  • cancelar — abortar la solicitud en curso\n"
        "  • ayuda    — mostrar esta ayuda"
    )


def _menu_text() -> str:
    return (
        "=== Bot de Vacaciones — Obsidian Systems ===\n"
        "Elegí una opción:\n"
        "  1) Solicitar vacaciones\n"
        "  2) Consultar saldo de días\n"
        "  3) Ver mis últimas solicitudes\n"
        "  0) Salir\n"
        f"\n{_help_text()}"
    )


def start_session() -> tuple[Session, str]:
    session = Session()
    session.persist()
    return session, _menu_text()


def handle_message(session: Session, raw_message: str) -> tuple[str, bool]:
    """Procesa un mensaje y devuelve (respuesta, continuar)."""
    message = raw_message.strip()
    lower = message.lower()

    if lower in GLOBAL_COMMANDS:
        return _handle_global_command(session, lower)

    if session.state == State.MENU:
        return _handle_menu(session, message)

    if session.state == State.AWAITING_EMPLOYEE_ID:
        return _handle_employee_id(session, message)

    if session.state == State.AWAITING_START_DATE:
        return _handle_start_date(session, message)

    if session.state == State.AWAITING_END_DATE:
        return _handle_end_date(session, message)

    if session.state == State.AWAITING_REASON:
        return _handle_reason(session, message)

    if session.state == State.AWAITING_CONFIRMATION:
        return _handle_confirmation(session, message)

    if session.state == State.COMPLETED:
        session.state = State.MENU
        session.context = {}
        session.persist()
        return _menu_text(), True

    return "Estado desconocido. Escribí 'menu' para reiniciar.", True


def _handle_global_command(session: Session, command: str) -> tuple[str, bool]:
    if command == "ayuda":
        return _help_text(), True

    if command == "menu":
        session.state = State.MENU
        session.context = {}
        session.persist()
        return "Volviste al menú principal.\n\n" + _menu_text(), True

    session.state = State.MENU
    session.context = {}
    session.persist()
    return "Solicitud cancelada.\n\n" + _menu_text(), True


def _handle_menu(session: Session, message: str) -> tuple[str, bool]:
    if message == "1":
        session.state = State.AWAITING_EMPLOYEE_ID
        session.context = {}
        session.persist()
        return (
            "Ingresá tu número de legajo (solo números, ej: 1001).\n"
            "Podés usar 'cancelar' para volver al menú.",
            True,
        )

    if message == "2":
        session.state = State.AWAITING_EMPLOYEE_ID
        session.context = {"mode": "balance"}
        session.persist()
        return "Ingresá tu legajo para consultar saldo:", True

    if message == "3":
        session.state = State.AWAITING_EMPLOYEE_ID
        session.context = {"mode": "history"}
        session.persist()
        return "Ingresá tu legajo para ver tus solicitudes:", True

    if message == "0":
        return "¡Hasta luego!", False

    return (
        "Opción no válida. Ingresá 1, 2, 3 o 0.\n"
        "Si necesitás ayuda, escribí 'ayuda'.",
        True,
    )


def _handle_employee_id(session: Session, message: str) -> tuple[str, bool]:
    if not message.isdigit():
        return (
            "El legajo debe contener solo números.\n"
            "Reintentá o escribí 'cancelar'.",
            True,
        )

    employee = queries.get_employee_by_legajo(message)
    if not employee:
        return (
            f"No encontramos el legajo {message}.\n"
            "Verificá el número o contactá a RR.HH.\n"
            "Reintentá o escribí 'cancelar'.",
            True,
        )

    session.employee = employee
    mode = session.context.get("mode")

    if mode == "balance":
        session.state = State.MENU
        session.context = {}
        session.persist()
        return (
            f"Hola {employee['full_name']} ({employee['department']}).\n"
            f"Tu saldo disponible es: {employee['vacation_balance']} días hábiles.\n\n"
            + _menu_text(),
            True,
        )

    if mode == "history":
        requests = queries.get_employee_requests(employee["id"])
        session.state = State.MENU
        session.context = {}
        session.persist()
        if not requests:
            body = "No tenés solicitudes registradas."
        else:
            lines = []
            for req in requests:
                lines.append(
                    f"  #{req['id']} | {req['start_date']} → {req['end_date']} | "
                    f"{req['days_requested']} días | {req['status']}"
                )
            body = "Últimas solicitudes:\n" + "\n".join(lines)
        return f"{body}\n\n{_menu_text()}", True

    session.state = State.AWAITING_START_DATE
    session.persist()
    return (
        f"Hola {employee['full_name']} ({employee['department']}).\n"
        f"Saldo disponible: {employee['vacation_balance']} días hábiles.\n"
        f"Ingresá la fecha de inicio ({DATE_FORMAT_HINT}):",
        True,
    )


def _handle_start_date(session: Session, message: str) -> tuple[str, bool]:
    start, error = parse_date(message)
    if error:
        return f"{error}\nReintentá o escribí 'cancelar'.", True

    range_error = validate_date_range(start, start)
    if range_error:
        return f"{range_error}\nReintentá o escribí 'cancelar'.", True

    session.context["start_date"] = start.isoformat()
    session.state = State.AWAITING_END_DATE
    session.persist()
    return f"Ingresá la fecha de fin ({DATE_FORMAT_HINT}):", True


def _handle_end_date(session: Session, message: str) -> tuple[str, bool]:
    end, error = parse_date(message)
    if error:
        return f"{error}\nReintentá o escribí 'cancelar'.", True

    start = date.fromisoformat(session.context["start_date"])
    range_error = validate_date_range(start, end)
    if range_error:
        return f"{range_error}\nReintentá o escribí 'cancelar'.", True

    days = business_days_between(start, end)
    balance = session.employee["vacation_balance"]

    if days > balance:
        return (
            f"Solicitás {days} días hábiles pero tu saldo es {balance}.\n"
            "Ajustá las fechas o escribí 'cancelar'.",
            True,
        )

    session.context["end_date"] = end.isoformat()
    session.context["days_requested"] = days
    session.state = State.AWAITING_REASON
    session.persist()
    return (
        f"Pediste {days} día(s) hábil(es) del {start.strftime('%d/%m/%Y')} "
        f"al {end.strftime('%d/%m/%Y')}.\n"
        "Ingresá un motivo breve (mínimo 3 caracteres):",
        True,
    )


def _handle_reason(session: Session, message: str) -> tuple[str, bool]:
    if len(message) < 3:
        return "El motivo debe tener al menos 3 caracteres.", True

    session.context["reason"] = message
    session.state = State.AWAITING_CONFIRMATION
    session.persist()

    start = date.fromisoformat(session.context["start_date"])
    end = date.fromisoformat(session.context["end_date"])
    days = session.context["days_requested"]
    approval = (
        "aprobación automática"
        if days <= AUTO_APPROVE_THRESHOLD
        else "aprobación del gerente (pendiente)"
    )

    return (
        "Resumen de la solicitud:\n"
        f"  Empleado : {session.employee['full_name']}\n"
        f"  Desde    : {start.strftime('%d/%m/%Y')}\n"
        f"  Hasta    : {end.strftime('%d/%m/%Y')}\n"
        f"  Días     : {days}\n"
        f"  Motivo   : {message}\n"
        f"  Destino  : {approval}\n\n"
        "¿Confirmás la solicitud? (si/no)",
        True,
    )


def _handle_confirmation(session: Session, message: str) -> tuple[str, bool]:
    lower = message.lower()
    if lower not in {"si", "sí", "s", "no", "n"}:
        return "Respondé 'si' o 'no'.", True

    if lower in {"no", "n"}:
        session.state = State.MENU
        session.context = {}
        session.persist()
        return "Solicitud descartada.\n\n" + _menu_text(), True

    days = session.context["days_requested"]
    status = "APPROVED" if days <= AUTO_APPROVE_THRESHOLD else "PENDING"
    start = date.fromisoformat(session.context["start_date"])
    end = date.fromisoformat(session.context["end_date"])

    try:
        request = queries.create_vacation_request(
            employee_id=session.employee["id"],
            start_date=start,
            end_date=end,
            days_requested=days,
            reason=session.context["reason"],
            status=status,
        )
    except ValueError as exc:
        return f"No se pudo registrar: {exc}\n\n" + _menu_text(), True

    session.employee["vacation_balance"] = request["remaining_balance"]
    session.state = State.COMPLETED
    session.context = {}
    session.persist()

    if status == "APPROVED":
        outcome = (
            f"✓ Solicitud #{request['id']} APROBADA automáticamente.\n"
            f"Saldo restante: {request['remaining_balance']} días."
        )
    else:
        outcome = (
            f"⏳ Solicitud #{request['id']} registrada como PENDIENTE.\n"
            "Un gerente debe aprobarla (más de "
            f"{AUTO_APPROVE_THRESHOLD} días hábiles).\n"
            f"Saldo reservado. Restante: {request['remaining_balance']} días."
        )

    return outcome + "\n\n" + _menu_text(), True
