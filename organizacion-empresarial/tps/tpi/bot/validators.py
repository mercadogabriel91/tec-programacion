"""Validaciones de reglas de negocio."""

from __future__ import annotations

from datetime import date, datetime


DATE_FORMAT = "%d/%m/%Y"


def parse_date(value: str) -> tuple[date | None, str | None]:
    cleaned = value.strip()
    try:
        parsed = datetime.strptime(cleaned, DATE_FORMAT).date()
    except ValueError:
        return None, f"Formato inválido. Usá {DATE_FORMAT} (ejemplo: 15/07/2026)."

    if parsed.weekday() >= 5:
        return None, "Las fechas deben ser días hábiles (lunes a viernes)."

    return parsed, None


def business_days_between(start: date, end: date) -> int:
    if end < start:
        return 0

    total = 0
    current = start
    while current <= end:
        if current.weekday() < 5:
            total += 1
        current = date.fromordinal(current.toordinal() + 1)
    return total


def validate_date_range(start: date, end: date, today: date | None = None) -> str | None:
    reference = today or date.today()
    if start < reference:
        return "La fecha de inicio no puede ser anterior a hoy."
    if end < start:
        return "La fecha de fin debe ser posterior o igual a la de inicio."
    days = business_days_between(start, end)
    if days == 0:
        return "El rango seleccionado no incluye días hábiles."
    return None
