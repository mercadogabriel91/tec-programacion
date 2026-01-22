# Interpreter: Python 3.12.3
import math

# ** COMO USAR **
# Simplemente des-comentar el llamado a la función que se quiera probar
# al pie del archivo y ejecutar main.py


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

    # ====================================================================


# EJERCICIO 6: [Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.]
# ====================================================================
# El código del ejercicio 6 aquí
def ejercicio_6():
    multiplier_list = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # Acá podría agregarse una validación del input para un número entero positivo como en el Ej 4
    number_to_multiply = int(
        input("Por favor ingrese un numero y a cambio recibirá la tabla de multiplicación del mismo:\n "))

    for number in multiplier_list:
        print(f"{number_to_multiply} x {number} = {number * number_to_multiply}\n")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 7: [Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.]
# ====================================================================
# El código del ejercicio 1 aquí
def ejercicio_7():
    def validate_input(message="Ingrese un número distinto de 0 \n"):
        """
        Requests that the user enters a non-zero number

        Args:
            message: the message to be displayed to the user

        Returns:
            int: a non-zero number
        """

        wrong_number_msg = "Error: El número debe distinto a 0. Intente nuevamente."
        wrong_input_msg = "Error: Debe ingresar un número válido. Intente nuevamente."

        while True:
            try:
                input_number = int(input(message))
                if input_number != 0:
                    print("Numero aceptado \n")
                    return input_number
                else:
                    print(wrong_number_msg)
            except ValueError:
                print(wrong_input_msg)

    numbers_to_multiply = []
    print("Bienvenido! se requieren dos números enteros para multiplicar")

    while len(numbers_to_multiply) < 2:
        numbers_to_multiply.append(int(validate_input()))

    print(
        f"el producto de multiplicar {numbers_to_multiply[0]} x {numbers_to_multiply[1]} es igual a {numbers_to_multiply[0] * numbers_to_multiply[1]}\n")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 8: [Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo: 𝐼𝑀𝐶 =
# 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
# 2
# (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)]
# ====================================================================
# El código del ejercicio 8 aquí
def ejercicio_8():
    weight = 0
    height = 0

    print("Calculadora de indice de masa corporal (IMC) \n")
    weight = float(input("Por favor ingrese su peso en Kg \n"))
    height = float(input("Por favor ingrese su altura en m (hasta 2 decimales separados por un punto: ej 1.85)\n"))

    print(f"El IMC calculado es de {weight / (height * height)}")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 9: [Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
# Despejamos la ecuación:
# Tc = 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠
# Tf = 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡
# Tc = (Tf - 32) / (9/5)]
# ====================================================================
# El código del ejercicio 9 aquí
def ejercicio_9():
    def convert_celsius_to_fahrenheit(celsius_degrees):
        return (celsius_degrees * 9 / 5) + 32

    print("Calculadora equivalencia °F a °C \n")

    c_degrees = int(input("Por favor ingrese un numero en grados 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 (°C) \n"))
    fahrenheit_degrees = convert_celsius_to_fahrenheit(c_degrees)

    print(f"El equivalente a {c_degrees} °C en °F es igual a {fahrenheit_degrees}\n")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 10: [Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.]
# ====================================================================
# El código del ejercicio 10 aquí
def ejercicio_10():
    numbers_list = []

    def validate_input(message="Ingrese un número entero positivo:  \n"):
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
                    print("Numero aceptado \n")
                    return input_number
                else:
                    print(wrong_number_msg)
            except ValueError:
                print(wrong_input_msg)

    print("Por favor ingrese tres numeros y se calculará un promedio sobre ellos \n")

    while len(numbers_list) < 3:
        numbers_list.append(validate_input())

    if len(numbers_list) != 0:
        print(
            f" el promedio es estos 3 numeros es: {(numbers_list[0] + numbers_list[1] + numbers_list[2]) / len(numbers_list)} \n")

    return 0
    # Fin


# ejercicio_1()
# ejercicio_2()
# ejercicio3()
# ejercicio_4()
# ejercicio_5()
# ejercicio_6()
# ejercicio_7()
# ejercicio_8()
# ejercicio_9()
# ejercicio_10()

# GitHub url for the repository.
# https://github.com/mercadogabriel91/tec-programacion
