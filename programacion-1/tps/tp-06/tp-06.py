import math
from typing import Tuple

# ** COMO USAR **
# Simplemente des-comentar el llamado a la función que se quiera probar
# al pie del archivo y ejecutar tp-06.py

# ====================================================================
# Ejercicio 1: Función imprimir_hola_mundo que muestra "Hola Mundo!" en consola.
# ====================================================================
def imprimir_hola_mundo() -> None:
    hello_world_string: str = "Hola mundo!"
    print(hello_world_string);


def ejercicio_1() -> int:
    imprimir_hola_mundo();
    print();

    return 0;
    # Fin


# ====================================================================
# Ejercicio 2: Función saludar_usuario(nombre) que devuelve un saludo personalizado.
# ====================================================================
def saludar_usuario(nombre: str) -> str:
    return f"Hola {nombre}!";


def ejercicio_2() -> int:
    nombre: str = input("Ingrese su nombre: ").strip();
    saludo: str = saludar_usuario(nombre);
    print(saludo);
    print();

    return 0;
    # Fin


# ====================================================================
# Ejercicio 3: Función informacion_personal(nombre, apellido, edad, residencia).
# ====================================================================
def informacion_personal(
    nombre: str, apellido: str, edad: int, residencia: str
) -> None:
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}");


def ejercicio_3():
    nombre: str = input("Nombre: ").strip();
    apellido: str = input("Apellido: ").strip();
    edad: int = int(input("Edad: ").strip());
    residencia: str = input("Lugar de residencia: ").strip();

    informacion_personal(nombre, apellido, edad, residencia);
    print();

    return 0;
    # Fin


# ====================================================================
# Ejercicio 4: Área y perímetro de un círculo a partir del radio.
# ====================================================================
def calcular_area_circulo(radio: float) -> float:
    return math.pi * radio * radio;


def calcular_perimetro_circulo(radio: float) -> float:
    return 2.0 * math.pi * radio;


def ejercicio_4():
    radio: float = float(input("Ingrese el radio del círculo: ").strip());
    area: float = calcular_area_circulo(radio);
    perimetro: float = calcular_perimetro_circulo(radio);

    print(f"\nÁrea: {area}");
    print(f"Perímetro: {perimetro}\n");

    return 0;
    # Fin


# ====================================================================
# Ejercicio 5: Función segundos_a_horas(segundos).
# ====================================================================
def segundos_a_horas(segundos: float) -> float:
    SEG_EN_HORA: float = 3600;

    return segundos / SEG_EN_HORA;


def ejercicio_5():
    segundos: float = float(input("Ingrese la cantidad de segundos: ").strip());
    horas: float = segundos_a_horas(segundos);

    print(f"\nEquivale a {horas} hora(s).\n");

    return 0;
    # Fin


# ====================================================================
# Ejercicio 6: Función tabla_multiplicar(numero) del 1 al 10.
# ====================================================================
def tabla_multiplicar(numero: int) -> None:
    print(f"\nTabla de multiplicar del {numero}:\n")
    for i in range(1, 11):
        resultado: int = numero * i;
        print(f"  {numero} x {i} = {resultado}");


def ejercicio_6():
    numero: int = int(input("Ingrese un número: ").strip());
    tabla_multiplicar(numero);
    print();

    return 0;
    # Fin


# ====================================================================
# Ejercicio 7: Función operaciones_basicas(a, b) que devuelve suma, resta, producto y cociente.
# ====================================================================
def operaciones_basicas(a: float, b: float) -> Tuple[float, float, float, float]:
    suma: float = a + b;
    resta: float = a - b;
    producto: float = a * b;
    cociente: float = a / b;
    return (suma, resta, producto, cociente);


def ejercicio_7():
    a: float = float(input("Primer número: ").strip());
    b: float = float(input("Segundo número: ").strip());
    suma, resta, producto, cociente = operaciones_basicas(a, b);

    print(f"\nSuma: {suma}");
    print(f"Resta: {resta}");
    print(f"Producto: {producto}");
    print(f"Cociente: {cociente}\n");

    return 0;
    # Fin


# ====================================================================
# Ejercicio 8: Función índice de masa corporal calcular_imc(peso, altura); resultado con dos decimales.
# ====================================================================
def calcular_imc(peso: float, altura: float) -> float:
    return peso / (altura * altura);


def ejercicio_8():
    peso: float = float(input("Peso (kg): ").strip());
    altura: float = float(input("Altura (m): ").strip());
    imc: float = calcular_imc(peso, altura);

    print(f"\nIMC: {imc:.2f}\n");

    return 0;
    # Fin


# ====================================================================
# Ejercicio 9: Función celsius_a_fahrenheit(celsius).
# ====================================================================
def celsius_a_fahrenheit(celsius: float) -> float:
    return (celsius * 9.0 / 5.0) + 32.0;


def ejercicio_9():
    celsius: float = float(input("Temperatura en °C: ").strip());
    fahrenheit: float = celsius_a_fahrenheit(celsius);

    print(f"\n{fahrenheit} °F\n");

    return 0;
    # Fin


# ====================================================================
# Ejercicio 10: Función calcular_promedio(a, b, c).
# ====================================================================
def calcular_promedio(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3.0;


def ejercicio_10():
    a: float = float(input("Primer número: ").strip());
    b: float = float(input("Segundo número: ").strip());
    c: float = float(input("Tercer número: ").strip());
    promedio: float = calcular_promedio(a, b, c);

    print(f"\nPromedio: {promedio}\n");

    return 0;
    # Fin


# Repository:
# https://github.com/mercadogabriel91/tec-programacion
# ejercicio_1();
# ejercicio_2();
# ejercicio_3();
# ejercicio_4();
# ejercicio_5();
# ejercicio_6();
# ejercicio_7();
# ejercicio_8();
# ejercicio_9();
# ejercicio_10();
