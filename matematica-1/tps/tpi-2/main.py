"""Programa de consola: regiones de un diagrama de Venn con 3 conjuntos.

TPI-2 Matematica 1 — Conjuntos y diagramas de Venn.

Pide al usuario el universo U, los conjuntos A, B y C, sus cardinalidades
e intersecciones, calcula las regiones exclusivas y (opcionalmente) guarda
un diagrama de Venn en PNG.
"""

from conjuntos import (
    DatosConjuntos,
    EntradaInvalidaError,
    calcular_regiones,
    validar_entero_no_negativo,
    validar_texto,
)
from diagrama import generar_diagrama_venn

MENU = """
*******************************************
   DIAGRAMA DE VENN — 3 CONJUNTOS
*******************************************
 1. Calcular regiones del diagrama
 2. Ejemplo: YouTube / ChatGPT / Moodle
 0. Salir
"""

# Datos de ejemplo (misma estructura numerica que el ejemplo orientativo)
EJEMPLO = DatosConjuntos(
    desc_u="totalidad de estudiantes del curso de Matematica de la TUP a Distancia",
    desc_a="estudiantes que utilizan YouTube para estudiar",
    desc_b="estudiantes que utilizan ChatGPT",
    desc_c="estudiantes que utilizan Moodle",
    card_u=40,
    card_a=10,
    card_b=20,
    card_c=5,
    card_ab=4,
    card_ac=2,
    card_bc=3,
    card_abc=1,
)


def pedir_datos() -> DatosConjuntos:
    """Le pide al usuario que meta todos los datos del problema."""
    print("\n--- Datos del universo y los conjuntos ---\n")

    desc_u = validar_texto(input("Descripcion del universo U: "), "U")
    card_u = validar_entero_no_negativo(input("|U| (cantidad total): "), "|U|")

    desc_a = validar_texto(input("Descripcion del conjunto A: "), "A")
    card_a = validar_entero_no_negativo(input("|A|: "), "|A|")

    desc_b = validar_texto(input("Descripcion del conjunto B: "), "B")
    card_b = validar_entero_no_negativo(input("|B|: "), "|B|")

    desc_c = validar_texto(input("Descripcion del conjunto C: "), "C")
    card_c = validar_entero_no_negativo(input("|C|: "), "|C|")

    print("\n--- Intersecciones ---\n")
    card_ab = validar_entero_no_negativo(input("|A ∩ B|: "), "|A ∩ B|")
    card_ac = validar_entero_no_negativo(input("|A ∩ C|: "), "|A ∩ C|")
    card_bc = validar_entero_no_negativo(input("|B ∩ C|: "), "|B ∩ C|")
    card_abc = validar_entero_no_negativo(input("|A ∩ B ∩ C|: "), "|A ∩ B ∩ C|")

    return DatosConjuntos(
        desc_u=desc_u,
        desc_a=desc_a,
        desc_b=desc_b,
        desc_c=desc_c,
        card_u=card_u,
        card_a=card_a,
        card_b=card_b,
        card_c=card_c,
        card_ab=card_ab,
        card_ac=card_ac,
        card_bc=card_bc,
        card_abc=card_abc,
    )


def mostrar_resultados(datos: DatosConjuntos) -> None:
    """Calcula, imprime los pasos y ofrece guardar el diagrama."""
    regiones, pasos = calcular_regiones(datos)

    print("\n========================================")
    print("  RESOLUCION PASO A PASO")
    print("========================================")
    print(f"U = {datos.desc_u}   (|U| = {datos.card_u})")
    print(f"A = {datos.desc_a}   (|A| = {datos.card_a})")
    print(f"B = {datos.desc_b}   (|B| = {datos.card_b})")
    print(f"C = {datos.desc_c}   (|C| = {datos.card_c})")
    print(
        f"|A ∩ B| = {datos.card_ab}   |A ∩ C| = {datos.card_ac}   "
        f"|B ∩ C| = {datos.card_bc}   |A ∩ B ∩ C| = {datos.card_abc}"
    )
    print()
    for paso in pasos:
        print(f"  {paso}")

    print("\n========================================")
    print("  REGIONES DEL DIAGRAMA")
    print("========================================")
    print(f"  Solo A:            {regiones.solo_a}")
    print(f"  Solo B:            {regiones.solo_b}")
    print(f"  Solo C:            {regiones.solo_c}")
    print(f"  Solo A ∩ B:        {regiones.solo_ab}")
    print(f"  Solo A ∩ C:        {regiones.solo_ac}")
    print(f"  Solo B ∩ C:        {regiones.solo_bc}")
    print(f"  A ∩ B ∩ C:         {regiones.abc}")
    print(f"  En al menos uno:   {regiones.en_alguno}")
    print(f"  Ninguno:           {regiones.ninguno}")

    respuesta = input(
        "\nGenerar diagrama de Venn en PNG? (s/n): "
    ).strip().lower()
    if respuesta in ("s", "si", "sí", "y", "yes"):
        ruta = generar_diagrama_venn(datos, regiones)
        print(f"Diagrama guardado en: {ruta}")


def main() -> None:
    acciones = {
        "1": lambda: mostrar_resultados(pedir_datos()),
        "2": lambda: mostrar_resultados(EJEMPLO),
    }

    while True:
        print(MENU)
        opcion = input("Elija una opción: ").strip()

        if opcion == "0":
            print("saliendo...")
            break

        accion = acciones.get(opcion)
        if accion is None:
            print(f"Error: '{opcion}' no es una opción válida. Elija 1, 2 o 0.")
            continue

        try:
            accion()
        except EntradaInvalidaError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma finalizado.")
