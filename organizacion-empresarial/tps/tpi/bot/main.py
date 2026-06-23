"""Punto de entrada del chatbot de vacaciones (simulador CLI)."""

import sys
import time

from bot.db.connection import get_connection
from bot.handlers.conversation import handle_message, start_session


def wait_for_db(retries: int = 30, delay: float = 1.0) -> None:
    for attempt in range(retries):
        try:
            with get_connection():
                return
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(delay)


def run() -> None:
    wait_for_db()
    session, greeting = start_session()
    print(greeting)

    while True:
        try:
            user_input = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n¡Hasta luego!")
            break

        if not user_input:
            print("Ingresá un mensaje o escribí 'ayuda'.")
            continue

        response, should_continue = handle_message(session, user_input)
        print("\n" + response)

        if not should_continue:
            break


if __name__ == "__main__":
    run()
