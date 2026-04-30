# ====================================================================
# EJERCICIO 1: [Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.]
# ====================================================================
# El código del ejercicio 1 aquí
def ejercicio_1():
    age = int(input("Por favor ingrese su edad: \n"))
    if age >= 18:
        print("Es mayor de edad \n")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 2: [Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”]
# ====================================================================
# El código del ejercicio 2 aquí
def ejercicio_2():
    grade = int(input("Por favor ingrese su nota: \n"))
    if grade >= 6:
        print("Aprobado \n")
    else:
        print("Desaprobado \n")

    return 0
    # Fin

    # ====================================================================


# EJERCICIO 3: [Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.]
# ====================================================================
# El código del ejercicio 3 aquí
def ejercicio_3():
    is_even: bool = False
    please_enter_even_number: str = "Por favor ingrese un numero par  \n"
    that_is_odd: str = "Ha ingresado un número par. \n"

    def check_even_number(input_number: int) -> bool:
        if input_number % 2 == 0:
            return True
        else:
            return False

    while not is_even:
        my_num = int(input(please_enter_even_number))
        is_even = check_even_number(my_num)

    print(that_is_odd)
    return 0
    # Fin


# ====================================================================
# EJERCICIO 4: [Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# • Niño/a: menor de 12 años.
# • Adolescente: mayor o igual que 12 años y menor que 18 años.
# • Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# • Adulto/a: mayor o igual que 30 años.]
# ====================================================================
# El código del ejercicio 4 aquí
def ejercicio_4():
    age = int(input("Por favor ingrese su edad indicada en años: \n"))

    if age < 12:
        print("Niño/a \n")
    elif 12 <= age < 18:
        print("Adolescente \n")
    elif 18 <= age < 30:
        print("Adulto/a joven \n")
    elif age >= 300:
        print("Mirtha? \n")
    else:
        print("Adulto/a \n")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 5: [Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".]
# ====================================================================
# El código del ejercicio 5 aquí
def ejercicio_5():
    is_valid_password: bool = False
    please_enter_password: str = "Por favor, ingrese una contraseña de entre 8 y 14 caracteres \n"
    password_correct: str = "Ha ingresado una contraseña correcta \n"

    while not is_valid_password:
        password = input(please_enter_password)
        password_length = len(password)

        if 8 <= password_length <= 14:
            is_valid_password = True
            print(password_correct)
        else:
            print(please_enter_password)

    return 0
    # Fin


# ====================================================================
# EJERCICIO 6: [Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en
# kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio:
# • Menor que 150 kWh: “Consumo bajo”.
# • Entre 150 y 300 kWh (inclusive): “Consumo medio”.
# • Mayor que 300 kWh: “Consumo alto”.]
# Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga:
# “Considere medidas de ahorro energético”.
# ====================================================================
# El código del ejercicio 6 aquí
def ejercicio_6():
    consumption = float(input("Por favor ingrese su consumo mensual de energía eléctrica en kWh: \n"))

    if consumption < 150:
        print("Consumo bajo \n")
    elif 150 <= consumption <= 300:
        print("Consumo medio \n")
    else:
        print("Consumo alto \n")

    if consumption > 500:
        print("Considere medidas de ahorro energético \n")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 7: [Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.]
# ====================================================================
# El código del ejercicio 7 aquí
def ejercicio_7():
    text = input("Por favor ingrese una frase o palabra: \n")

    if len(text) > 0:
        last_char = text[-1].lower()
        vowels = ['a', 'e', 'i', 'o', 'u']

        if last_char in vowels:
            text = text + "!"
    else:
        print("Texto ingresado vacío \n")

    print(text + "\n")
    return 0
    # Fin


# ====================================================================
# EJERCICIO 8: [Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.]
# ====================================================================
# El código del ejercicio 8 aquí
def ejercicio_8():
    nombre = input("Por favor ingrese su nombre: \n")
    options = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para primera letra mayúscula: \n"))
    invalid_potion = "Opción inválida \n"

    if options == 1:
        print(nombre.upper() + "\n")
    elif options == 2:
        print(nombre.lower() + "\n")
    elif options == 3:
        print(nombre.capitalize() + "\n")
    else:
        print(invalid_potion)

    return 0
    # Fin

    # ====================================================================


# EJERCICIO 9: [Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# Menor que 3: "Muy leve" (imperceptible).
# Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).]
# ====================================================================
# El código del ejercicio 9 aquí
def ejercicio_9():
    magnitude = float(input("Por favor ingrese la magnitud del terremoto en la escala de Richter: \n"))

    if magnitude < 3:
        print("Muy leve (imperceptible) \n")
    elif magnitude < 4:
        print("Leve (ligeramente perceptible) \n")
    elif magnitude < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños) \n")
    elif magnitude < 6:
        print("Fuerte (puede causar daños en estructuras débiles) \n")
    elif magnitude < 7:
        print("Muy Fuerte (puede causar daños significativos) \n")
    else:
        print("Extremo (puede causar graves daños a gran escala) \n")

    return 0
    # Fin


# ====================================================================
# EJERCICIO 10: [Utilizando la información aportada en la tabla del documento PDF sobre las estaciones del año,
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.]
# ====================================================================
# El código del ejercicio 10 aquí
def ejercicio_10():
    hemisphere = input("¿En qué hemisferio se encuentra? (N/S): \n").upper()
    month = int(input("¿Qué mes del año es? (1-12): \n"))
    day = int(input("¿Qué día es? (1-31): \n"))

    winter = "Invierno"
    spring = "Primavera"
    summer = "Verano"
    autumn = "Otoño"

    # Período 1: 21 dic - 20 mar → Norte: Invierno, Sur: Verano
    # Período 2: 21 mar - 20 jun → Norte: Primavera, Sur: Otoño
    # Período 3: 21 jun - 20 sep → Norte: Verano, Sur: Invierno
    # Período 4: 21 sep - 20 dic → Norte: Otoño, Sur: Primavera

    if (month == 12 and day >= 21) or month in (1, 2) or (month == 3 and day <= 20):
        season = winter if hemisphere == "N" else summer
    elif (month == 3 and day >= 21) or month in (4, 5) or (month == 6 and day <= 20):
        season = spring if hemisphere == "N" else autumn
    elif (month == 6 and day >= 21) or month in (7, 8) or (month == 9 and day <= 20):
        season = summer if hemisphere == "N" else winter
    elif (month == 9 and day >= 21) or month in (10, 11) or (month == 12 and day <= 20):
        season = autumn if hemisphere == "N" else spring
    else:
        season = "Fecha inválida"

    print(season + "\n")
    return 0
    # Fin

# URL al repositorio:
# https://github.com/mercadogabriel91/tec-programacion

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
