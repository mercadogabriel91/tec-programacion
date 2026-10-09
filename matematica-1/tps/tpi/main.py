from conversor import (
    EntradaInvalidaError,
    binario_a_decimal,
    decimal_a_binario,
    validar_binario,
    validar_decimal,
)

MENU = """
*******************************************
   CONVERSOR DECIMAL <-> BINARIO
*******************************************
 1. DE: Decimal A: Binario
 2. DE: Binario A: Decimal
 0. Salir
"""


def opcion_decimal_a_binario():
    numero = validar_decimal(input("Ingrese un numero decimal entero: "))
    binario, pasos = decimal_a_binario(numero)

    print("\nDivisiones sucesivas entre 2:")
    for dividendo, cociente, resto in pasos:
        print(f"  {dividendo:>10} / 2 = {cociente:<10} resto {resto}")
    print("  (se leen los restos de abajo hacia arriba)")

    print(f"\nResultado: {numero} (decimal) = {binario} (binario)")


def opcion_binario_a_decimal():
    signo, digitos = validar_binario(input("Ingrese un número binario: "))
    decimal, pasos = binario_a_decimal(signo, digitos)

    print("\nSuma de potencias de 2:")
    for bit, exponente, valor in pasos:
        print(f"  {bit} x 2^{exponente:<3} = {valor}")
    suma = " + ".join(str(valor) for _, _, valor in pasos)
    print(f"  {'-' if signo < 0 else ''}({suma}) = {decimal}")

    binario = ("-" if signo < 0 else "") + digitos
    print(f"\nResultado: {binario} (binario) = {decimal} (decimal)")


def main():
    acciones = {"1": opcion_decimal_a_binario, "2": opcion_binario_a_decimal}

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
