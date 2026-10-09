"""convertir los numeros decimales a binarios y viceversa

Las conversiones se hacen "a mano"
"""

from typing import List, Tuple

DIGITOS_DECIMALES = "0123456789"
DIGITOS_BINARIOS = "01"


class EntradaInvalidaError(ValueError):
    """Te tira el error cuando el usuario mete un dato que no se puede convertir."""


def _separar_signo(texto: str) -> Tuple[int, str]:
    if texto[0] in "+-":
        signo = -1 if texto[0] == "-" else 1 # Op ternario si el texto es - entonces el valor es -1 de lo contrario 1
        # Acá esta sintaxis medio rara es slicing con esto le decimos a python que agarre desde el indice 1 hasta el final del string (osea el n completo)
        cuerpo = texto[1:]
        if not cuerpo:
            raise EntradaInvalidaError("Falta el número después del signo.")
        return signo, cuerpo
    return 1, texto


def validar_decimal(texto: str) -> int:
    texto = texto.strip()
    if not texto:
        raise EntradaInvalidaError("No podes meter un input vacio.")

    signo, cuerpo = _separar_signo(texto)

    if "." in cuerpo or "," in cuerpo:
        raise EntradaInvalidaError("Solo se admiten numeros enteros sin la coma o puntos decimales.")

    # Hace un loop para cada uno de los chars y se fija que estén incluidos en los numeros permitidos osea del 0 al 9
    invalidos = sorted({c for c in cuerpo if c not in DIGITOS_DECIMALES})
    if invalidos:
        raise EntradaInvalidaError(
            f"'{texto}' no es un número decimal válido. Caracteres no permitidos: {' '.join(invalidos)}"
        )

    return signo * int(cuerpo)


def validar_binario(texto: str) -> Tuple[int, str]:
    """Devuelve (signo, dígitos) de un número binario ingresado como texto."""
    texto = texto.strip()
    if not texto:
        raise EntradaInvalidaError("Necesitas ingresar algún valor.")

    signo, cuerpo = _separar_signo(texto)

    invalidos = sorted({c for c in cuerpo if c not in DIGITOS_BINARIOS})
    if invalidos:
        raise EntradaInvalidaError(
            f"'{texto}' no es un número binario: solo puede tener 0 y 1. "
            f"Caracteres no permitidos: {' '.join(invalidos)}"
        )

    return signo, cuerpo


def decimal_a_binario(numero: int) -> Tuple[str, List[Tuple[int, int, int]]]:
    """Convierte por divisiones sucesivas entre 2.

    Devuelve el binario y la lista de pasos (dividendo, cociente, resto).
    """
    if numero == 0:
        return "0", [(0, 0, 0)]

    pasos: List[Tuple[int, int, int]] = []
    restante = abs(numero)
    while restante > 0:
        cociente = restante // 2 # acá usamos este operador // porque le saca los decimales al numero te da el entero solamente
        """
            * Acá el operador matematico que normalmente usamos para ver par / impar
            * coincidentemente nos sirve para saber si el resto es 0 o 1 
            * la intuicion matematica acá nos dice que lo que normalmente hariamos sería:
            * restante (ej 13) // 2 = 6 ---> cociente = 6
            * Luego: 
            * resto = restante - ( 2 * cociente); ES DECIR: 13 - (2*6) = 1  ----- PERO para hacer esto mas facil usamos el remainder module op
        """
        resto = restante % 2
        pasos.append((restante, cociente, resto))
        restante = cociente

    # Los restos se leen de abajo hacia arriba
    binario = "".join(str(resto) for _, _, resto in reversed(pasos))
    if numero < 0:
        binario = "-" + binario
    return binario, pasos


def binario_a_decimal(signo: int, digitos: str) -> Tuple[int, List[Tuple[int, int, int]]]:
    """Convierte sumando cada bit multiplicado por su potencia de 2.

    Devuelve el decimal y la lista de pasos (bit, exponente, valor aportado).
    """
    pasos: List[Tuple[int, int, int]] = []
    total = 0
    for exponente, caracter in enumerate(reversed(digitos)):
        bit = int(caracter)
        valor = bit * 2 ** exponente
        pasos.append((bit, exponente, valor))
        total += valor

    pasos.reverse()
    return signo * total, pasos
