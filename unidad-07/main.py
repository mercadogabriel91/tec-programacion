from typing import List


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


# ejercicio_1()
# ejercicio_2()
# ejercicio_3()
ejercicio_4()
