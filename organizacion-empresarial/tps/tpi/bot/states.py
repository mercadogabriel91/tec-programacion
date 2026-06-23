"""Estados del flujo BPMN (máquina de estados del chatbot)."""

from enum import StrEnum


class State(StrEnum):
    MENU = "MENU"
    AWAITING_EMPLOYEE_ID = "AWAITING_EMPLOYEE_ID"
    AWAITING_START_DATE = "AWAITING_START_DATE"
    AWAITING_END_DATE = "AWAITING_END_DATE"
    AWAITING_REASON = "AWAITING_REASON"
    AWAITING_CONFIRMATION = "AWAITING_CONFIRMATION"
    COMPLETED = "COMPLETED"


# Comandos globales reconocidos en cualquier estado activo
GLOBAL_COMMANDS = frozenset({"cancelar", "menu", "ayuda"})

DATE_FORMAT_HINT = "DD/MM/AAAA"
