from typing import List
import random


# ====================================================================
# EJERCICIO 1: [Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.]
# ====================================================================
# El código del ejercicio 1 aquí
def ejercicio_1():
    n: int = 0
    max_iterations: int = 100

    while n < max_iterations + 1:
        print(f"{n} \n")
        n += 1

    return 0
    # Fin


# ====================================================================
# EJERCICIO 2: [Desarrolla un programa que solicite al usuario un número entero y determine la cantidad
# de dígitos que contiene.]
# ====================================================================
# El código del ejercicio 2 aquí
def ejercicio_2():
    def get_digits_string(number):
        # Convert the number to a string
        num_str = str(number)

        # Use a list comprehension to convert each character digit back to an integer
        # This also naturally handles negative signs by ignoring them in the conversion loop
        digits = [int(digit) for digit in num_str if digit.isdigit()]

        return digits

    user_input_number: int = int(input("Por favor ingrese un numero: \n"))
    print(f"La cantidad de dígitos en {user_input_number} es {len(get_digits_string(user_input_number))} \n")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 3: [Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.]
# ====================================================================
# El código del ejercicio 3 aquí
def ejercicio_3():
    program_instructions: str = "Este programa le pedirá dos números (enteros) y calculará la suma de los números comprendidos entre ellos: \n"

    print(program_instructions)
    n1 = int(input("Por favor ingrese el primer numero: \n"))
    n2 = int(input("Por favor ingrese el segundo numero: \n"))

    # El segundo número provisto debe ser mayor al primero o el "rango" será 0
    if n2 > n1:
        numbers_to_add: List[int] = []

        # Mientras el 2° sea mayor al 1° restar 1 y acumular en un array para luego sumarlos
        while n2 > n1 + 1:
            new_num: int = n2 - 1
            n2 -= 1
            numbers_to_add.append(new_num)

        print(f"La suma total es {sum(numbers_to_add)} \n")

    else:
        print("El segundo numero debe ser mayor al primero: \n")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 4: [Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario
# ingrese un 0.]
# ====================================================================
# El código del ejercicio 4 aquí
def ejercicio_4():
    counter: int = 0
    reading: bool = True
    initial_message: str = "El programa le pedirá que ingrese números y los sumará hasta que ingrese 0 o un input incorrecto: \n"
    exit_message: str = "El programa será finalizado...\n"

    print(initial_message)

    while reading:
        try:
            user_input_number = int(input("Por favor ingrese el numero: \n"))
        except ValueError:
            print("Valor no válido. Finalizando.")
            reading = False

            break
        if user_input_number != 0:
            counter += user_input_number
            print(f"La suma total hasta ahora es {counter} \n")
        else:
            print(exit_message)
            print(f"La suma final es {counter} \n")
            reading = False

    return 0
    # Fin


# ====================================================================
# EJERCICIO 5: [Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final,
# el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.]
# ====================================================================
# El código del ejercicio 5 aquí
def ejercicio_5():
    number_of_tries: int = 0
    number_to_guess: int = random.randint(0, 9)

    print("Adiviná el número entre 0 y 9. \n")

    while True:
        number_of_tries += 1
        guess: int = int(input("Tu intento: \n"))
        if guess == number_to_guess:
            print(f"Correcto! Lo adivinaste en {number_of_tries} intento(s).\n")

            break
        print("No es ese. Intentá de nuevo.\n")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 6: [Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.]
# ====================================================================
# El código del ejercicio 6 aquí
def ejercicio_6():
    for n in range(100, -1, -2):
        print(n)
    return 0
    # Fin


# ====================================================================
# EJERCICIO 7: [Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.]
# ====================================================================
# El código del ejercicio 7 aquí
def ejercicio_7():
    n: int = int(input("Ingresa un número entero positivo: \n"))

    if n < 0:
        print("El número debe ser positivo.\n")
        return 0
    total: int = sum(range(n + 1))
    print(f"La suma de 0 hasta {n} es {total}.\n")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 8: [Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos
# son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una
# cantidad menor, pero debe estar preparado para procesar 100 números con un solo
# cambio)]
# ====================================================================
# El código del ejercicio 8 aquí
def ejercicio_8():
    def is_even(number: int) -> bool:
        number: int = int(number)
        if number % 2 == 0:
            return True
        else:
            return False

    def is_positive(number: int) -> bool:
        number: int = int(number)
        if number > 0:
            return True
        else:
            return False

    def interrupt_execution(user_input: str) -> bool:
        """True and will interrupt if you input a letter"""
        try:
            int(user_input.strip())
            return False
        except ValueError:
            return True

    initial_message: str = "El programa le permitirá ingresar como maximo 100 números enteros para clasificar, puede finalizar el proceso ingresando una letra en cualquier momento \n"
    reading: bool = True
    counter: int = 0
    even_numbers_list = []
    odd_numbers_list = []
    even_negative_numbers_list = []
    even_positive_numbers_list = []
    odd_negative_numbers_list = []
    odd_positive_numbers_list = []

    print(initial_message)
    while reading and counter < 101:
        string_input: str = input("Ingrese un numero \n")
        if interrupt_execution(string_input):
            break
        else:
            captured_value = int(string_input)
            if captured_value != 0:
                if is_even(captured_value):
                    even_numbers_list.append(captured_value)
                    if is_positive(captured_value):
                        even_positive_numbers_list.append(captured_value)
                    else:
                        even_negative_numbers_list.append(captured_value)
                else:
                    odd_numbers_list.append(captured_value)
                    if is_positive(captured_value):
                        odd_positive_numbers_list.append(captured_value)
                    else:
                        odd_negative_numbers_list.append(captured_value)
            else:
                print("El 0 es un numero no invalido")

        print(
            f"Los numeros pares son {len(even_numbers_list)} de los cuales: {len(even_positive_numbers_list)} son positivos y {len(even_negative_numbers_list)} son negativos \n")
        print(
            f"Los numeros in-pares son {len(odd_numbers_list)} de los cuales: {len(odd_positive_numbers_list)} son positivos y {len(odd_negative_numbers_list)} son negativos \n")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 9: [Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule
# la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero
# debe poder procesar 100 números cambiando solo un valor).]
# ====================================================================
# El código del ejercicio 9 aquí
def ejercicio_9():
    amount: int = 100  # Cambiar solo este valor para probar con menos o más
    numbers_sum: int = 0

    print(f"Ingrese {amount} números enteros.")
    for i in range(amount):
        numbers_sum += int(input(f"Número {i + 1}/{amount}: "))

    average: float = numbers_sum / amount
    print(f"La media de los {amount} valores es {average}.")
    return 0
    # Fin


# ====================================================================
# EJERCICIO 10: [Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.]
# ====================================================================
# El código del ejercicio 10 aquí
def ejercicio_10():
    n: int = int(input("Ingrese un número entero: "))
    sign: int = -1 if n < 0 else 1
    digits: List[str] = list(str(abs(n)))
    digits.reverse()

    opposite: int = sign * int("".join(digits))
    print(f"Con dígitos invertidos: {opposite}")
    return 0
    # Fin

# ejercicio_1()
# ejercicio_2()
# ejercicio_3()
# ejercicio_4()
# ejercicio_5()
# ejercicio_6()
# ejercicio_7()
# ejercicio_8()
# ejercicio_9()
# ejercicio_10()
