# Interpreter: Python 3.12.3
import math


# ====================================================================
# EJERCICIO 1: [Hello world]
# ====================================================================
# El código del ejercicio 1 aquí
def ejercicio_1():
    print("Hola Mundo!")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 2: [Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.]
# ====================================================================
# El código del ejercicio 2 aquí
def ejercicio_2():
    name = input("Por favor ingrese su nombre\n")
    print(f"Hola {name}!")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 3: [Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.]
# ====================================================================
# El código del ejercicio 3 aquí
def ejercicio3():
    name = input("Por favor ingrese su nombre\n")
    lastname = input("Por favor ingrese su apellido\n")
    age = input("Por favor ingrese su edad\n")
    country = input("Por favor ingrese su país de origen\n")

    print(f"Soy {name} {lastname}, tengo {age} años y vivo en {country}")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 4: [Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.]
# ====================================================================
# El código del ejercicio 4 aquí
def ejercicio_4():
    pi_value = math.pi

    # Calculate area function
    def calculate_area(radius):
        return pi_value * radius ** 2

    # Calculate perimeter function
    def calculate_perimeter(radius):
        return 2 * pi_value * radius

    def validate_radius_input(message="Ingrese un número entero positivo: "):
        """
        Requests that the user enters a valid positive integer

        Args:
            message: the message to be displayed to the user

        Returns:
            int: a positive integer
        """

        wrong_number_msg = "Error: El número debe ser positivo (mayor que 0). Intente nuevamente."
        wrong_input_msg = "Error: Debe ingresar un número entero válido. Intente nuevamente."

        while True:
            try:
                input_number = int(input(message))
                if input_number > 0:
                    return input_number
                else:
                    print(wrong_number_msg)
            except ValueError:
                print(wrong_input_msg)

    # Ejemplo de uso:
    # edad = obtener_entero_positivo("Ingrese su edad: ")
    # print(f"Edad ingresada: {edad}")

    radius_input_string = "Por favor ingrese su radio, el mismo debe ser un numero entero\n"
    radius = validate_radius_input(radius_input_string)

    print(f"El área calculada para un radio de {radius} es de: {calculate_area(radius)} unidades de superficie\n")
    print(
        f"El perimetro calculado para un radio de {radius} es de {calculate_perimeter(radius)} unidades de superficie\n")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 5: [Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale]
# ====================================================================
# El código del ejercicio 5 aquí
def ejercicio_5():
    def convert_seconds_to_hours(secs):
        # 1 hour = 3600 seconds
        hour_in_seconds_eq = 3600
        hours = secs / hour_in_seconds_eq

        return hours

    # Ejemplo de uso:
    h = convert_seconds_to_hours(int(input("Ingrese el numero de segundos a convertir en horas:\n ")))
    print(f"{h} horas")

    return 0
    # Fin


# ejercicio_1()
# ejercicio_2()
# ejercicio3()
# ejercicio_4()
ejercicio_5()
