# Interpreter: Python 3.12.3

# ** COMO USAR **
# Simplemente des-comentar el llamado a la función que se quiera probar
# al pie del archivo y ejecutar tp-01.py


# ====================================================================
# EJERCICIO 1: [Caja del Kiosco]
# ====================================================================
# Simular una compra en un kiosco con validación de datos y cálculo de totales.
#
# 1) Nombre del cliente: solo letras; validar con .isalpha() en un while (no cadena vacía).
# 2) Cantidad de productos: entero positivo; validar con .isdigit() en un while (> 0).
# 3) Con un for, por cada producto: precio entero (.isdigit()); descuento S/N (while, aceptar
#    s/n en mayúsculas o minúsculas). Si hay descuento, aplicar 10 % a ese producto.
# 4) Mostrar: total sin descuentos, total con descuentos, ahorro total, promedio por producto
#    (usar float y f-strings con formato .2f donde corresponda).
#
# Restricción: no usar try/except para el manejo de errores.
#
# Ejemplo de salida:
# Cliente: Ana
# Cantidad de productos: 3
# Producto 1 - Precio: 100  Descuento (S/N): s
# Producto 2 - Precio: 50   Descuento (S/N): n
# Producto 3 - Precio: 200  Descuento (S/N): s
#
# Total sin descuentos: $350
# Total con descuentos: $320.00
# Ahorro: $30.00
# Promedio por producto: $106.67
# ====================================================================
# El código del ejercicio 1 aquí
def ejercicio_1():
    while True:
        nombre = input("Nombre del cliente: ").strip()
        if nombre != "" and nombre.isalpha():
            break
        print("Error: el nombre debe contener solo letras y no puede estar vacío.")

    print(f"Cliente: {nombre}")

    while True:
        cantidad_str = input("Cantidad de productos: ").strip()
        if cantidad_str.isdigit():
            cantidad = int(cantidad_str)
            if cantidad > 0:
                break
        print("Error: debe ingresar un entero positivo mayor que 0.")

    print(f"Cantidad de productos: {cantidad}")

    total_sin_descuentos = 0
    total_con_descuentos = 0.0

    for i in range(1, cantidad + 1):
        while True:
            precio_str = input(f"Producto {i} - Precio: ").strip()
            if precio_str.isdigit():
                precio = int(precio_str)
                break
            print("Error: el precio debe ser un número entero válido (solo dígitos).")

        while True:
            descuento = input(f"Producto {i} - Descuento (S/N): ").strip().lower()
            if descuento == "s" or descuento == "n":
                break
            print("Error: ingrese S o N (mayúsculas o minúsculas).")

        print(f"Producto {i} - Precio: {precio}  Descuento (S/N): {descuento}")

        total_sin_descuentos += precio
        if descuento == "s":
            total_con_descuentos += precio * 0.9
        else:
            total_con_descuentos += float(precio)

    ahorro = float(total_sin_descuentos) - total_con_descuentos
    promedio = total_con_descuentos / cantidad

    print()
    print(f"Total sin descuentos: ${total_sin_descuentos}")
    print(f"Total con descuentos: ${total_con_descuentos:.2f}")
    print(f"Ahorro: ${ahorro:.2f}")
    print(f"Promedio por producto: ${promedio:.2f}")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 2: []
# ====================================================================

# Login con intentos + menú de acciones con validación estricta.
#
# 1. Definir credenciales fijas en el código:
# o usuario correcto: "alumno"
# o clave correcta: "python123"
# 2. Permitir máximo 3 intentos para ingresar usuario y clave.
# 3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
# 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
# 1. Ver estado de inscripción (mostrar “Inscripto”)
# 2. Cambiar clave (pedir nueva clave y confirmación; deben
# coincidir)
# 3. Mostrar mensaje motivacional (1 frase)
# 4. Salir
# 5. Validación del menú:
# o Debe ser número (.isdigit())
# o Debe estar entre 1 y 4
# Cambio de clave
# • La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no,
# rechazar.
# ====================================================================
# El código del ejercicio 2 aquí
def ejercicio_2():
    default_credentials: dict[str, str] = {"user": "alumno", "password": "python123"}
    max_attempts: int = 3
    current_attempt: int = 0
    valid_credentials: bool = False

    def change_password() -> None:
        print(
            "Ha seleccionado la option de cambiar contraseña, por favor ingrese una nueva contraseña de al menos 6 caracteres \n")
        while True:
            min_password_length: int = 6
            new_password: str = input("\n")
            if len(new_password) < min_password_length:
                print("La contraseña no cumple los requisitos intente nuevamente. \n")
            else:
                default_credentials["password"] = new_password
                print("Contraseña cambiada exitosamente! \n")
                break

    def select_menu_option(option: int) -> None:
        match option:
            case 1:
                print("Estado de inscripción: Inscripto \n")
                return
            case 2:
                change_password()
                return
            case 3:
                print("Eso es un mensaje muy motivador! \n")
                return
            case 4:
                print("Saliendo...\n")
                return
            case _:
                print("Numero fuera de rango...\n")
                return

    while (valid_credentials == False) & (current_attempt <= max_attempts):
        print("Por favor ingrese sus credenciales: \n")
        input_user: str = input("Nombre del usuario: \n").strip()
        input_password: str = input("Contraseña: \n").strip()

        if (input_user == "" or input_password == "") or (
                input_user != default_credentials["user"] or input_password != default_credentials["password"]):
            print("Error: verifique que sus credenciales sean correctas.")
            current_attempt += 1
            print(current_attempt)
        else:
            print("Acceso concedido! \n")
            # Validate input is a digit or ask again
            while True:
                string_input: str = input(
                    "Por favor ingrese un numero para una opción, 1) Estado 2) Cambiar clave 3) Mensaje 4) Salir \n")

                if string_input.isdigit():
                    menu_input = int(string_input)
                    select_menu_option(menu_input)
                    break
                else:
                    print("Error: Eso no es un número válido. Intentalo de nuevo.")

            valid_credentials = True

    if not valid_credentials and max_attempts <= current_attempt:
        print("Cuenta bloqueada")
        return 0

    return 0
    # Fin


# ====================================================================
# EJERCICIO 3: [Agenda de Turnos con Nombres (sin listas)]
# ====================================================================
# Contexto:
# Hay 2 días de atención: Lunes y Mártes.
# Cada día tiene cupos fijos:
# - Lúnes: 4 turnos
# - Mártes: 3 turnos
#
# Reglas:
# 1) Pedir nombre del operador (solo letras).
# 2) Menú repetitivo hasta salir:
#    1. Reservar turno
#    2. Cancelar turno (por nombre)
#    3. Ver agenda del día
#    4. Ver resumen general
#    5. Cerrar sistema
# 3) Reservar:
#    - Elegir día (1=Lúnes, 2=Mártes).
#    - Pedir nombre del paciente (solo letras).
#    - Verificar que no esté repetido ese día.
#    - Guardar en el primer espacio libre.
# 4) Cancelar:
#    - Elegir día.
#    - Pedir nombre del paciente (solo letras).
#    - Si existe, cancelar y dejar el espacio vacío ("").
# 5) Ver agenda del día:
#    - Mostrar turnos del día en orden, indicando "libre" si está vacío.
# 6) Resumen general:
#    - Turnos ocupados y disponibles por día.
#    - Día con más turnos (o empate).
#
# Restricciones:
# - No listas, no diccionarios, no sets, no tuplas.
# - Se permite usar "" como "vacío".
# - Validaciones con .isalpha() y .isdigit() (sin try/except).
# ====================================================================
# El código del ejercicio 3 aquí
def ejercicio_3():
    monday_1: str = ""
    monday_2: str = ""
    monday_3: str = ""
    monday_4: str = ""

    tuesday_1: str = ""
    tuesday_2: str = ""
    tuesday_3: str = ""

    def ask_operator_name() -> str:
        while True:
            operator_name: str = input("Por favor ingrese nombre del operador: \n").strip()
            if operator_name != "" and operator_name.isalpha():
                return operator_name
            print("Error: el nombre debe tener solo letras y no puede estar vacío.\n")

    def ask_day() -> int:
        while True:
            day_input: str = input("Seleccione día 1) Lunes 2) Martes\n").strip()
            if day_input.isdigit():
                day_number: int = int(day_input)
                if day_number == 1 or day_number == 2:
                    return day_number
            print("Error: debe ingresar 1 para Lunes o 2 para Martes.\n")

    def ask_patient_name() -> str:
        while True:
            patient_name: str = input("Ingrese nombre del paciente: \n").strip()
            if patient_name != "" and patient_name.isalpha():
                return patient_name
            print("Error: el nombre del paciente debe tener solo letras y no puede estar vacío.\n")

    def is_repeated_name(day: int, name: str) -> bool:
        normalized_name: str = name.lower()

        if day == 1:
            return (
                    monday_1.lower() == normalized_name
                    or monday_2.lower() == normalized_name
                    or monday_3.lower() == normalized_name
                    or monday_4.lower() == normalized_name
            )

        return (
                tuesday_1.lower() == normalized_name
                or tuesday_2.lower() == normalized_name
                or tuesday_3.lower() == normalized_name
        )

    def reserve_turn() -> None:
        nonlocal monday_1, monday_2, monday_3, monday_4
        nonlocal tuesday_1, tuesday_2, tuesday_3

        selected_day: int = ask_day()
        patient_name: str = ask_patient_name()

        if is_repeated_name(selected_day, patient_name):
            print("Error: ese paciente ya tiene turno en ese día.\n")
            return

        if selected_day == 1:
            if monday_1 == "":
                monday_1 = patient_name
                print("Turno reservado en Lunes - Turno 1.\n")
                return
            if monday_2 == "":
                monday_2 = patient_name
                print("Turno reservado en Lunes - Turno 2.\n")
                return
            if monday_3 == "":
                monday_3 = patient_name
                print("Turno reservado en Lunes - Turno 3.\n")
                return
            if monday_4 == "":
                monday_4 = patient_name
                print("Turno reservado en Lunes - Turno 4.\n")
                return

            print("No hay turnos disponibles para Lunes.\n")
            return

        if tuesday_1 == "":
            tuesday_1 = patient_name
            print("Turno reservado en Martes - Turno 1.\n")
            return
        if tuesday_2 == "":
            tuesday_2 = patient_name
            print("Turno reservado en Martes - Turno 2.\n")
            return
        if tuesday_3 == "":
            tuesday_3 = patient_name
            print("Turno reservado en Martes - Turno 3.\n")
            return

        print("No hay turnos disponibles para Martes.\n")

    def cancel_turn() -> None:
        nonlocal monday_1, monday_2, monday_3, monday_4
        nonlocal tuesday_1, tuesday_2, tuesday_3

        selected_day: int = ask_day()
        patient_name: str = ask_patient_name()
        normalized_name: str = patient_name.lower()

        if selected_day == 1:
            if monday_1.lower() == normalized_name:
                monday_1 = ""
                print("Turno cancelado correctamente.\n")
                return
            if monday_2.lower() == normalized_name:
                monday_2 = ""
                print("Turno cancelado correctamente.\n")
                return
            if monday_3.lower() == normalized_name:
                monday_3 = ""
                print("Turno cancelado correctamente.\n")
                return
            if monday_4.lower() == normalized_name:
                monday_4 = ""
                print("Turno cancelado correctamente.\n")
                return

            print("No se encontró ese nombre en la agenda de Lunes.\n")
            return

        if tuesday_1.lower() == normalized_name:
            tuesday_1 = ""
            print("Turno cancelado correctamente.\n")
            return
        if tuesday_2.lower() == normalized_name:
            tuesday_2 = ""
            print("Turno cancelado correctamente.\n")
            return
        if tuesday_3.lower() == normalized_name:
            tuesday_3 = ""
            print("Turno cancelado correctamente.\n")
            return

        print("No se encontró ese nombre en la agenda de Martes.\n")

    def view_day_schedule() -> None:
        selected_day: int = ask_day()

        if selected_day == 1:
            print("Agenda de Lunes:")
            print(f"Turno 1: {monday_1 if monday_1 != '' else 'libre'}")
            print(f"Turno 2: {monday_2 if monday_2 != '' else 'libre'}")
            print(f"Turno 3: {monday_3 if monday_3 != '' else 'libre'}")
            print(f"Turno 4: {monday_4 if monday_4 != '' else 'libre'}\n")
            return

        print("Agenda de Martes:")
        print(f"Turno 1: {tuesday_1 if tuesday_1 != '' else 'libre'}")
        print(f"Turno 2: {tuesday_2 if tuesday_2 != '' else 'libre'}")
        print(f"Turno 3: {tuesday_3 if tuesday_3 != '' else 'libre'}\n")

    def day_occupied_count(day: int) -> int:
        occupied_count: int = 0

        if day == 1:
            if monday_1 != "":
                occupied_count += 1
            if monday_2 != "":
                occupied_count += 1
            if monday_3 != "":
                occupied_count += 1
            if monday_4 != "":
                occupied_count += 1
            return occupied_count

        if tuesday_1 != "":
            occupied_count += 1
        if tuesday_2 != "":
            occupied_count += 1
        if tuesday_3 != "":
            occupied_count += 1
        return occupied_count

    def view_general_summary() -> None:
        monday_occupied: int = day_occupied_count(1)
        tuesday_occupied: int = day_occupied_count(2)

        monday_available: int = 4 - monday_occupied
        tuesday_available: int = 3 - tuesday_occupied

        print("Resumen general de turnos:")
        print(f"Lunes -> Ocupados: {monday_occupied} | Disponibles: {monday_available}")
        print(f"Martes -> Ocupados: {tuesday_occupied} | Disponibles: {tuesday_available}")

        if monday_occupied > tuesday_occupied:
            print("Día con más turnos: Lunes.\n")
        elif tuesday_occupied > monday_occupied:
            print("Día con más turnos: Martes.\n")
        else:
            print("Día con más turnos: empate.\n")

    operator_name_value: str = ask_operator_name()
    print(f"Operador activo: {operator_name_value}\n")

    while True:
        menu_input: str = input(
            "Menú: 1) Reservar 2) Cancelar 3) Ver agenda del día 4) Ver resumen 5) Cerrar sistema\n"
        ).strip()

        if not menu_input.isdigit():
            print("Error: debe ingresar un número válido.\n")
            continue

        selected_option: int = int(menu_input)
        if selected_option < 1 or selected_option > 5:
            print("Error: opción fuera de rango. Elija entre 1 y 5.\n")
            continue

        if selected_option == 1:
            reserve_turn()
        elif selected_option == 2:
            cancel_turn()
        elif selected_option == 3:
            view_day_schedule()
        elif selected_option == 4:
            view_general_summary()
        else:
            print("Sistema cerrado.\n")
            break

    return 0
    # Fin


# ====================================================================
# EJERCICIO 4: [Escape Room: La Bóveda]
# ====================================================================
# Simulación de escape room con 3 cerraduras, energía/tiempo limitados y alarma.
#
# Variables iniciales:
# - energia = 100
# - tiempo = 12
# - cerraduras_abiertas = 0
# - alarma = False
# - codigo_parcial = ""
#
# Validaciones obligatorias:
# - Nombre del agente con .isalpha() en while.
# - Opción de menú con .isdigit() en while.
# - Sin try/except.
#
# Reglas principales:
# 1) Forzar cerradura: costo -20 energía y -2 tiempo.
#    - Si energía < 40, hay riesgo de alarma (pedir número 1..3; si elige 3 -> alarma=True).
#    - Si no hay alarma, abre 1 cerradura.
#    - Anti-spam: si se usa 3 veces seguidas, se cobra costo, NO abre y alarma=True.
# 2) Hackear panel: costo -10 energía y -3 tiempo.
#    - for de 4 pasos mostrando progreso.
#    - En cada paso suma una letra al código.
#    - Si len(codigo_parcial) >= 8 y faltan cerraduras, abre 1 automáticamente.
# 3) Descansar: +15 energía (máx 100), -1 tiempo.
#    - Si alarma está activa: -10 energía extra.
#
# Bloqueo por alarma:
# - Si alarma=True, tiempo<=3 y aún no se abrió la bóveda, derrota por bloqueo.
#
# Fin:
# - cerraduras_abiertas == 3 -> VICTORIA
# - energia <= 0 o tiempo <= 0 -> DERROTA
# ====================================================================
# El código del ejercicio 4 aquí
def ejercicio_4():
    energy: int = 100
    time_left: int = 12
    opened_locks: int = 0
    alarm_on: bool = False
    partial_code: str = ""
    force_streak: int = 0
    blocked_by_alarm: bool = False

    def ask_agent_name() -> str:
        while True:
            agent_name: str = input("Ingrese nombre del agente: \n").strip()
            if agent_name != "" and agent_name.isalpha():
                return agent_name
            print("Error: el nombre debe contener solo letras y no puede estar vacío.\n")

    def ask_menu_option() -> int:
        while True:
            option_input: str = input("Menú: 1) Forzar 2) Hackear 3) Descansar\n").strip()
            if option_input.isdigit():
                option_number: int = int(option_input)
                if option_number >= 1 and option_number <= 3:
                    return option_number
            print("Error: debe ingresar una opción válida (1, 2 o 3).\n")

    def ask_risk_number() -> int:
        while True:
            risk_input: str = input("Riesgo de alarma: elija un número del 1 al 3\n").strip()
            if risk_input.isdigit():
                risk_number: int = int(risk_input)
                if risk_number >= 1 and risk_number <= 3:
                    return risk_number
            print("Error: debe ingresar un número válido entre 1 y 3.\n")

    agent_name_value: str = ask_agent_name()
    print(f"Agente activo: {agent_name_value}\n")

    while energy > 0 and time_left > 0 and opened_locks < 3 and not blocked_by_alarm:
        print(
            f"Estado -> Energía: {energy} | Tiempo: {time_left} | Cerraduras abiertas: {opened_locks} | Alarma: {alarm_on}")
        selected_option: int = ask_menu_option()

        if selected_option == 1:
            energy -= 20
            time_left -= 2
            force_streak += 1

            if force_streak >= 3:
                alarm_on = True
                print("Regla anti-spam: la cerradura se trabó. Se activó la alarma y no se abrió cerradura.\n")
            else:
                if energy < 40 and not alarm_on:
                    risk_value: int = ask_risk_number()
                    if risk_value == 3:
                        alarm_on = True
                        print("Se activó la alarma por riesgo.\n")

                if not alarm_on and opened_locks < 3:
                    opened_locks += 1
                    print(f"Cerradura abierta correctamente. Total abiertas: {opened_locks}\n")
                elif alarm_on:
                    print("No se abrió cerradura porque la alarma está activa.\n")

        elif selected_option == 2:
            energy -= 10
            time_left -= 3
            force_streak = 0

            for step in range(1, 5):
                partial_code += "A"
                print(f"Hackeo en progreso... paso {step}/4 | Código parcial: {partial_code}")

            if len(partial_code) >= 8 and opened_locks < 3:
                opened_locks += 1
                print(f"Se abrió una cerradura automáticamente por código. Total abiertas: {opened_locks}\n")
            else:
                print("Hackeo completado. Aún no se abrió cerradura automática.\n")

        else:
            time_left -= 1
            force_streak = 0

            energy += 15
            if energy > 100:
                energy = 100

            if alarm_on:
                energy -= 10
                print("Descanso con alarma activa: se aplicó penalización adicional de energía.\n")
            else:
                print("Descanso aplicado correctamente.\n")

        if alarm_on and time_left <= 3 and opened_locks < 3:
            blocked_by_alarm = True
            print("El sistema se bloqueó por alarma antes de abrir la bóveda.\n")

    if opened_locks == 3:
        print("VICTORIA: abriste las 3 cerraduras a tiempo.\n")
    elif blocked_by_alarm:
        print("DERROTA (bloqueo): la alarma bloqueó el sistema.\n")
    elif energy <= 0 or time_left <= 0:
        print("DERROTA: te quedaste sin energía o sin tiempo.\n")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 5: [La Arena del Gladiador]
# ====================================================================
# Simulador de combate por turnos: gladiador (usuario) vs enemigo (CPU).
#
# Tipos: str nombre, int HP y pociones, float para daño (crítico x1.5), bool turno/activo.
# Validación: nombre con .isalpha() en while; menú con .isdigit() en while (1..3).
# Sin try/except.
#
# Inicial (fijo): HP gladiador 100, HP enemigo 100, 3 pociones, daño base pesado 15,
# daño enemigo 12, turno gladiador True.
#
# Menú: 1 Ataque Pesado (si HP enemigo < 20 -> crítico float x1.5), 2 Ráfaga (for 3x, -5 c/u),
# 3 Curar (+30 HP, -1 poción; sin pociones: mensaje y pierde turno de acción útil; igual ataca el enemigo).
# Tras la acción del jugador, si el enemigo sigue vivo, contraataca con 12.
# Fin: victoria si gladiador > 0 y enemigo <= 0; derrota si gladiador <= 0.
# ====================================================================
# El código del ejercicio 5 aquí
def ejercicio_5():
    gladiator_name: str = ""
    gladiator_hp: int = 100
    enemy_hp: int = 100
    potions_left: int = 3
    heavy_attack_base: int = 15
    enemy_base_damage: int = 12
    is_gladiator_turn: bool = True
    game_active: bool = True
    max_gladiator_hp: int = 100
    is_first_round: bool = True

    def ask_gladiator_name() -> str:
        while True:
            name_input: str = input("Ingrese el nombre del gladiador: \n").strip()
            if name_input != "" and name_input.isalpha():
                return name_input
            print("Error: Solo se permiten letras.\n")

    def ask_menu_option() -> int:
        while True:
            menu_input: str = input(
                "Menú: 1) Ataque Pesado 2) Ráfaga Veloz 3) Curar\n"
            ).strip()
            if menu_input.isdigit():
                menu_number: int = int(menu_input)
                if menu_number == 1 or menu_number == 2 or menu_number == 3:
                    return menu_number
            print("Error: Ingrese un número válido.\n")

    print("--- BIENVENIDO A LA ARENA ---\n")
    gladiator_name = ask_gladiator_name()

    while game_active and gladiator_hp > 0 and enemy_hp > 0:
        if is_first_round:
            print("=== INICIO DEL COMBATE ===\n")
            is_first_round = False
        else:
            print("=== NUEVO TURNO ===\n")

        is_gladiator_turn = True
        print(
            f"{gladiator_name} (HP: {gladiator_hp}) vs Enemigo (HP: {enemy_hp}) | Pociones: {potions_left}\n"
        )

        selected_action: int = ask_menu_option()

        if selected_action == 1:
            damage_value: float = float(heavy_attack_base)
            if enemy_hp < 20:
                damage_value = float(heavy_attack_base) * 1.5
            damage_applied: int = int(damage_value)
            enemy_hp -= damage_applied
            print(f"Atacaste al enemigo por {damage_applied} puntos de daño!\n")

        elif selected_action == 2:
            print(">> Inicias una ráfaga de golpes!\n")
            for _hit in range(3):
                enemy_hp -= 5
                print("> Golpe conectado por 5 de daño\n")

        else:
            if potions_left > 0:
                gladiator_hp += 30
                if gladiator_hp > max_gladiator_hp:
                    gladiator_hp = max_gladiator_hp
                potions_left -= 1
            else:
                print("No quedan pociones!\n")

        is_gladiator_turn = False

        if enemy_hp <= 0:
            game_active = False
            break

        gladiator_hp -= enemy_base_damage
        print(f"El enemigo te atacó por {enemy_base_damage} puntos de daño!\n")

        if gladiator_hp <= 0:
            game_active = False
            break

    if gladiator_hp > 0:
        print(f"VICTORIA! {gladiator_name} ha ganado la batalla.\n")
    else:
        print("DERROTA. Has caído en combate.\n")

    return 0
    # Fin

# ejercicio_1()
# ejercicio_2()
# ejercicio_3()
# ejercicio_4()
# ejercicio_5()
