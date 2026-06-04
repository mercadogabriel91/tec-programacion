from typing import Dict, List, Set, Tuple

# ** COMO USAR **
# Simplemente des-comentar el llamado a la función que se quiera probar
# al pie del archivo y ejecutar tp-07.py

# ====================================================================
# Ejercicio 1: Inicializar diccionario de precios de frutas y agregar nuevas.
# ====================================================================
def inicializar_precios_frutas() -> Dict[str, int]:
    precios_frutas: Dict[str, int] = {
        "Banana": 1200,
        "Ananá": 2500,
        "Melón": 3000,
        "Uva": 1450,
    };
    precios_frutas["Naranja"] = 1200;
    precios_frutas["Manzana"] = 1500;
    precios_frutas["Pera"] = 2300;

    return precios_frutas;


def ejercicio_1() -> int:
    precios_frutas: Dict[str, int] = inicializar_precios_frutas();
    print(precios_frutas);
    print();

    return 0;
    # Fin


# ====================================================================
# Ejercicio 2: Actualizar precios de frutas en el diccionario.
# ====================================================================
def actualizar_precios_frutas(precios_frutas: Dict[str, int]) -> Dict[str, int]:
    precios_frutas["Banana"] = 1330;
    precios_frutas["Manzana"] = 1700;
    precios_frutas["Melón"] = 2800;
    return precios_frutas;


def ejercicio_2() -> int:
    precios_frutas: Dict[str, int] = inicializar_precios_frutas();
    precios_frutas = actualizar_precios_frutas(precios_frutas);
    print(precios_frutas);
    print();

    return 0;
    # Fin


# ====================================================================
# Ejercicio 3: Extraer las claves del diccionario de frutas a una lista.
# ====================================================================
def obtener_nombres_frutas(precios_frutas: Dict[str, int]) -> List[str]:
    return list(precios_frutas.keys());


def ejercicio_3() -> int:
    precios_frutas: Dict[str, int] = inicializar_precios_frutas();
    precios_frutas = actualizar_precios_frutas(precios_frutas);
    nombres_frutas: List[str] = obtener_nombres_frutas(precios_frutas);
    print(nombres_frutas);
    print();

    return 0;
    # Fin


# ====================================================================
# Ejercicio 4: Agenda telefónica: cargar 5 contactos y consultar por nombre.
# ====================================================================
def cargar_contactos(cantidad: int) -> Dict[str, str]:
    contactos: Dict[str, str] = {};
    for i in range(1, cantidad + 1):
        nombre: str = input(f"Nombre del contacto {i}: ").strip();
        telefono: str = input(f"Teléfono de {nombre}: ").strip();
        contactos[nombre] = telefono;
    return contactos;


def consultar_contacto(contactos: Dict[str, str], nombre: str) -> str:
    if nombre in contactos:
        return contactos[nombre];
    return "Contacto no encontrado";


def ejercicio_4() -> int:
    contactos: Dict[str, str] = cargar_contactos(5);
    nombre: str = input("\nIngrese el nombre a consultar: ").strip();
    resultado: str = consultar_contacto(contactos, nombre);
    print(f"\n{resultado}\n");

    return 0;
    # Fin


# ====================================================================
# Ejercicio 5: Palabras únicas (set) y recuento de apariciones (dict) en una frase.
# ====================================================================
def analizar_frase(frase: str) -> Tuple[Set[str], Dict[str, int]]:
    palabras: List[str] = frase.split();
    palabras_unicas: Set[str] = set(palabras);
    recuento: Dict[str, int] = {};
    for palabra in palabras:
        recuento[palabra] = recuento.get(palabra, 0) + 1;

    return (palabras_unicas, recuento);


def ejercicio_5() -> int:
    frase: str = input("Ingrese una frase: ").strip();
    palabras_unicas, recuento = analizar_frase(frase);
    print(f"\nPalabras_únicas: {palabras_unicas}");
    print(f"Recuento: {recuento}\n");

    return 0;
    # Fin


# ====================================================================
# Ejercicio 6: Alumnos con tupla de 3 notas; mostrar promedio de cada uno.
# ====================================================================
def calcular_promedio_notas(notas: Tuple[int, int, int]) -> float:
    return sum(notas) / len(notas);


def cargar_alumnos(cantidad: int) -> Dict[str, Tuple[int, int, int]]:
    alumnos: Dict[str, Tuple[int, int, int]] = {};

    for i in range(1, cantidad + 1):
        nombre: str = input(f"Nombre del alumno {i}: ").strip();
        nota_1: int = int(input(f"Nota 1 de {nombre}: ").strip());
        nota_2: int = int(input(f"Nota 2 de {nombre}: ").strip());
        nota_3: int = int(input(f"Nota 3 de {nombre}: ").strip());
        alumnos[nombre] = (nota_1, nota_2, nota_3);

    return alumnos;


def ejercicio_6() -> int:
    alumnos: Dict[str, Tuple[int, int, int]] = cargar_alumnos(3);
    print();
    for nombre, notas in alumnos.items():
        promedio: float = calcular_promedio_notas(notas);
        print(f"{nombre}: promedio = {promedio}");
    print();

    return 0;
    # Fin


# ====================================================================
# Ejercicio 7: Lista de asistencias: original, set único y recuento por empleado.
# ====================================================================
def procesar_asistencias(asistencias: List[str]) -> Tuple[Set[str], Dict[str, int]]:
    empleados_unicos: Set[str] = set(asistencias);
    recuento: Dict[str, int] = {};

    for nombre in asistencias:
        recuento[nombre] = recuento.get(nombre, 0) + 1;

    return (empleados_unicos, recuento);


def ejercicio_7() -> int:
    asistencias: List[str] = [
        "Olivia",
        "Alfonso",
        "Olivia",
        "María",
        "Alfonso",
        "Raul",
        "Olivia",
    ];

    empleados_unicos, recuento = procesar_asistencias(asistencias);

    print(f"Lista original: {asistencias}");
    print(f"Asistieron al menos una vez: {empleados_unicos}");
    print(f"Recuento por empleado: {recuento}");
    print();

    return 0;
    # Fin


# ====================================================================
# Ejercicio 8: Stock de productos: consultar, agregar unidades o nuevo producto.
# ====================================================================
def consultar_stock(stock: Dict[str, int], producto: str) -> int:
    return stock.get(producto, 0);


def agregar_al_stock(stock: Dict[str, int], producto: str, unidades: int) -> Dict[str, int]:
    if producto in stock:
        stock[producto] += unidades;
    else:
        stock[producto] = unidades;
    return stock;


def ejercicio_8() -> int:
    stock: Dict[str, int] = {
        "arroz": 50,
        "fideos": 30,
        "aceite": 20,
    };

    producto: str = input("Producto a consultar o actualizar: ").strip().lower();
    unidades: int = int(input("Unidades a agregar: ").strip());

    print(f"\nStock actual de '{producto}': {consultar_stock(stock, producto)}");
    stock = agregar_al_stock(stock, producto, unidades);
    print(f"Stock actualizado: {stock}\n");

    return 0;
    # Fin


# ====================================================================
# Ejercicio 9: Agenda con claves (día, hora) y consulta de actividad.
# ====================================================================
def consultar_agenda(
    agenda: Dict[Tuple[str, str], str], dia: str, hora: str
) -> str:
    clave: Tuple[str, str] = (dia, hora);

    if clave in agenda:
        return agenda[clave];

    return "Sin actividad programada";


def ejercicio_9() -> int:
    agenda: Dict[Tuple[str, str], str] = {
        ("lunes", "10:00"): "Reunión",
        ("martes", "15:00"): "Practica de C++",
    };

    dia: str = input("Día: ").strip();
    hora: str = input("Hora (ej. 10:00): ").strip();

    actividad: str = consultar_agenda(agenda, dia, hora);

    print(f"\n{actividad}\n");

    return 0;
    # Fin


# ====================================================================
# Ejercicio 10: Invertir diccionario país -> capital a capital -> país.
# ====================================================================
def invertir_diccionario(original: Dict[str, str]) -> Dict[str, str]:
    invertido: Dict[str, str] = {};

    for pais, capital in original.items():
        invertido[capital] = pais;

    return invertido;


def ejercicio_10() -> int:
    original: Dict[str, str] = {
        "Argentina": "Buenos Aires",
        "Chile": "Santiago",
        "China": "Beijing"
    };

    invertido: Dict[str, str] = invertir_diccionario(original);

    print(f"Original: {original}");
    print(f"Invertido: {invertido}\n");

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
# jercicio_10();
