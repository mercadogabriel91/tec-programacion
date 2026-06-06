# ** COMO USAR **
# Simplemente des-comentar el llamado a la función que se quiera probar
# al pie del archivo y ejecutar tp-08.py

# ====================================================================
# Ejercicio 1: Identificar errores en los fragmentos con comentarios.
# ====================================================================
def fragmento_division_con_error() -> None:
    a: int = 10;
    b: str = input("Introduce un número: "); # acá debería intentar convertirse a valor numérico y hacer un saneamiento del input
    result = a / b;  # Error: TypeError. 'b' es un string y no permite la división.
    print(f"Resultado: {result}");


def fragmento_lista_con_error() -> None:
    numbers: list[int] = [1, 2, 3];
    print(numbers[5]);  # Error: IndexError. El índice 5 no existe en una lista de 3 elementos.


def ejercicio_1() -> int:
    print("Fragmento 1 - división:");
    print("  Línea con error: result = a / b");
    print("  Tipo: TypeError. input() devuelve str y no se puede dividir int / str.");
    print("\n");
    print("Fragmento 2 - lista:");
    print("  Línea con error: print(numbers[5])");
    print("  Tipo: IndexError. Índices válidos: 0, 1 y 2.");
    print("\n");

    return 0;
    # Fin


# ====================================================================
# Ejercicio 2: Corregir el código del ejercicio 1 sin usar excepciones.
# ====================================================================
def division_corregida(a: int, b_texto: str) -> float:
    if (b_texto != "0"):
        b: float = float(b_texto);

        return a / b;
    else:
        print("No se puede dividir por 0 y existe un error puntual para manejar esto");
        return 0;


def lista_corregida(numbers: list[int], indice: int) -> int:
    return numbers[indice];


def ejercicio_2() -> int:
    a: int = 10;
    b_texto: str = input("Introduce un número: ").strip();
    result: float = division_corregida(a, b_texto);
    print(f"Resultado: {result}");

    numbers: list[int] = [1, 2, 3];
    indice: int = 2; # Debe ser como máximo el valorr de longitud del array menos 1
    print(f"Elemento en índice [{indice}]: {lista_corregida(numbers, indice)}");
    print();

    return 0;
    # Fin


# ====================================================================
# Ejercicio 3: Mantener errores originales y usar try-except genérico.
# ====================================================================
def division_con_try_except(a: int, b_texto: str) -> None:
    b: str = b_texto;
    try:
        result = a / b;
        print(f"Resultado: {result}");
    except Exception as error:
        print(f"Error en división: {error}");


def lista_con_try_except(numbers: list[int], indice: int) -> None:
    try:
        print(numbers[indice]);
    except Exception as error:
        print(f"Error en lista: {error}");


def ejercicio_3() -> int:
    b_texto: str = input("Introduce un número: ").strip();
    division_con_try_except(10, b_texto);

    numbers: list[int] = [1, 2, 3];
    lista_con_try_except(numbers, 5);
    print();

    return 0;
    # Fin


# ====================================================================
# Ejercicio 4: try-except con excepciones múltiples específicas.
# ====================================================================
def division_con_excepciones_especificas(a: int, b_texto: str) -> None:
    b: str = b_texto;
    try:
        result = a / b;
        print(f"Resultado: {result}");
    except TypeError as error:
        print(f"TypeError en división: {error}");
    except ZeroDivisionError as error:
        print(f"ZeroDivisionError en división: {error}");


def lista_con_excepciones_especificas(numbers: list[int], indice: int) -> None:
    try:
        print(numbers[indice]);
    except IndexError as error:
        print(f"IndexError en lista: {error}");
    except TypeError as error:
        print(f"TypeError en lista: {error}");


def ejercicio_4() -> int:
    b_texto: str = input("Introduce un número: ").strip();
    division_con_excepciones_especificas(10, b_texto);

    numbers: list[int] = [1, 2, 3];
    lista_con_excepciones_especificas(numbers, 5);
    print();

    return 0;
    # Fin


# ====================================================================
# Ejercicio 5: Repetir ejercicio 4 con bloques else y finally.
# ====================================================================
def division_con_else_finally(a: int, b_texto: str) -> None:
    b: str = b_texto;

    try:
        result = a / b;
    except TypeError as error:
        print(f"TypeError en división: {error}");
    except ZeroDivisionError as error:
        print(f"ZeroDivisionError en división: {error}");
    else:
        print(f"Resultado: {result}");
    finally:
        print("Fin del intento de división. Esta salida estará siempre porque viene de finally");


def lista_con_else_finally(numbers: list[int], indice: int) -> None:
    try:
        elemento = numbers[indice];
    except IndexError as error:
        print(f"IndexError en lista: {error}");
    except TypeError as error:
        print(f"TypeError en lista: {error}");
    else:
        print(f"Elemento: {elemento}");
    finally:
        print("Fin del bloque de lista. Finally en linea 160");


def ejercicio_5() -> int:
    b_texto: str = input("Introduce un número: ").strip();
    division_con_else_finally(10, b_texto);

    numbers: list[int] = [1, 2, 3];
    lista_con_else_finally(numbers, 5);
    print();

    return 0;
    # Fin


# ====================================================================
# Ejercicio 6: Pedir un número; manejar valor inválido y errores inesperados.
# ====================================================================
def leer_numero_usuario() -> None:
    try:
        valor_texto: str = input("Ingrese un número: ").strip();
        numero: float = float(valor_texto);
        print(numero);
    except ValueError:
        print("Debe ingresar un número válido");
    except Exception as error:
        print(f"Se produjo un error inesperado: {error}");


def ejercicio_6() -> int:
    leer_numero_usuario();
    print();

    return 0;
    # Fin


# ====================================================================
# Ejercicio 7: Repetir ejercicio 6 con reintento tras un error.
# ====================================================================
def leer_numero_usuario_con_reintento() -> None:
    while True:
        try:
            valor_texto: str = input("Ingrese un número: ").strip();
            numero: float = float(valor_texto);
            print(numero);
            break;
        except ValueError:
            print("Debe ingresar un número válido");
        except Exception as error:
            print(f"Se produjo un error inesperado: {error}");
            break;


def ejercicio_7() -> int:
    leer_numero_usuario_con_reintento();
    print();

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
