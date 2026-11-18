"""Calculo de regiones de un diagrama de Venn con 3 conjuntos.

A partir de las cardinalidades de U, A, B, C y de las intersecciones
|A ∩ B|, |A ∩ C|, |B ∩ C| y |A ∩ B ∩ C|, se obtienen las 7 regiones
exclusivas del diagrama y la cantidad de elementos fuera de A ∪ B ∪ C.
"""

from dataclasses import dataclass
from typing import List, Tuple


class EntradaInvalidaError(ValueError):
    """Se lanza cuando el usuario ingresa un dato que no se puede usar."""


@dataclass
class DatosConjuntos:
    """Datos de entrada del problema (descripciones + cardinalidades)."""

    desc_u: str
    desc_a: str
    desc_b: str
    desc_c: str
    card_u: int
    card_a: int
    card_b: int
    card_c: int
    card_ab: int
    card_ac: int
    card_bc: int
    card_abc: int


@dataclass
class RegionesVenn:
    """Las 7 regiones exclusivas del Venn mas los que no estan en ninguno."""

    solo_a: int
    solo_b: int
    solo_c: int
    solo_ab: int
    solo_ac: int
    solo_bc: int
    abc: int
    ninguno: int
    en_alguno: int


def validar_texto(texto: str, campo: str) -> str:
    """Se fija que la descripcion no este vacia."""
    texto = texto.strip()
    if not texto:
        raise EntradaInvalidaError(f"La descripcion de '{campo}' no puede estar vacia.")
    return texto


def validar_entero_no_negativo(texto: str, campo: str) -> int:
    """Convierte un string a un numro entero positivo o lanza EntradaInvalidaError."""
    texto = texto.strip()
    if not texto:
        raise EntradaInvalidaError(f"Te falta el valor de '{campo}'. No puede estar vacio.")

    if "." in texto or "," in texto:
        raise EntradaInvalidaError(
            f"'{campo}' Tiene que ser un numero entero (sin decimales). Ingresado: '{texto}'."
        )

    if texto[0] in "+-":
        signo = texto[0]
        cuerpo = texto[1:]
        if not cuerpo:
            raise EntradaInvalidaError(f"Falta el numero despues del signo en '{campo}'.")
        if signo == "-":
            raise EntradaInvalidaError(f"'{campo}' no puede ser negativo. Recibido: '{texto}'.")
        texto = cuerpo

    if not texto.isdigit():
        invalidos = sorted({c for c in texto if not c.isdigit()})
        raise EntradaInvalidaError(
            f"'{texto}' no es un entero valido para '{campo}'. "
            f"Caracteres no permitidos: {' '.join(invalidos)}"
        )

    return int(texto)


def _verificar_consistencia(datos: DatosConjuntos) -> None:
    """Controla que las cardinalidades tengan sentido matematico."""
    u = datos.card_u
    a, b, c = datos.card_a, datos.card_b, datos.card_c
    ab, ac, bc = datos.card_ab, datos.card_ac, datos.card_bc
    abc = datos.card_abc

    if a > u:
        raise EntradaInvalidaError(f"|A|={a} no puede ser mayor que |U|={u}.")
    if b > u:
        raise EntradaInvalidaError(f"|B|={b} no puede ser mayor que |U|={u}.")
    if c > u:
        raise EntradaInvalidaError(f"|C|={c} no puede ser mayor que |U|={u}.")

    if ab > a or ab > b:
        raise EntradaInvalidaError(
            f"|A ∩ B|={ab} no puede superar a |A|={a} ni a |B|={b}."
        )
    if ac > a or ac > c:
        raise EntradaInvalidaError(
            f"|A ∩ C|={ac} no puede superar a |A|={a} ni a |C|={c}."
        )
    if bc > b or bc > c:
        raise EntradaInvalidaError(
            f"|B ∩ C|={bc} no puede superar a |B|={b} ni a |C|={c}."
        )

    if abc > ab or abc > ac or abc > bc:
        raise EntradaInvalidaError(
            f"|A ∩ B ∩ C|={abc} no puede superar a las intersecciones "
            f"|A ∩ B|={ab}, |A ∩ C|={ac} o |B ∩ C|={bc}."
        )


def calcular_regiones(datos: DatosConjuntos) -> Tuple[RegionesVenn, List[str]]:
    """Calcula las regiones exclusivas del Venn y devuelve los pasos escritos.

    Formulas (iguales al ejemplo orientativo de la consigna):

        Solo A ∩ B = |A ∩ B| - |A ∩ B ∩ C|
        Solo A ∩ C = |A ∩ C| - |A ∩ B ∩ C|
        Solo B ∩ C = |B ∩ C| - |A ∩ B ∩ C|
        Solo A     = |A| - Solo A∩B - Solo A∩C - |A ∩ B ∩ C|
        Solo B     = |B| - Solo A∩B - Solo B∩C - |A ∩ B ∩ C|
        Solo C     = |C| - Solo A∩C - Solo B∩C - |A ∩ B ∩ C|
        En alguno  = suma de las 7 regiones
        Ninguno    = |U| - En alguno
    """
    _verificar_consistencia(datos)

    a, b, c = datos.card_a, datos.card_b, datos.card_c
    ab, ac, bc = datos.card_ab, datos.card_ac, datos.card_bc
    abc = datos.card_abc
    u = datos.card_u

    pasos: List[str] = []

    solo_ab = ab - abc
    pasos.append(f"Solo A ∩ B: {ab} - {abc} = {solo_ab}")

    solo_ac = ac - abc
    pasos.append(f"Solo A ∩ C: {ac} - {abc} = {solo_ac}")

    solo_bc = bc - abc
    pasos.append(f"Solo B ∩ C: {bc} - {abc} = {solo_bc}")

    solo_a = a - solo_ab - solo_ac - abc
    pasos.append(
        f"Solo A: {a} - ({ab} - {abc}) - ({ac} - {abc}) - {abc} = {solo_a}"
    )

    solo_b = b - solo_ab - solo_bc - abc
    pasos.append(
        f"Solo B: {b} - ({ab} - {abc}) - ({bc} - {abc}) - {abc} = {solo_b}"
    )

    solo_c = c - solo_ac - solo_bc - abc
    pasos.append(
        f"Solo C: {c} - ({ac} - {abc}) - ({bc} - {abc}) - {abc} = {solo_c}"
    )

    # Si alguna region exclusiva queda negativa, los datos son inconsistentes
    negativos = {
        "Solo A": solo_a,
        "Solo B": solo_b,
        "Solo C": solo_c,
        "Solo A ∩ B": solo_ab,
        "Solo A ∩ C": solo_ac,
        "Solo B ∩ C": solo_bc,
    }
    for nombre, valor in negativos.items():
        if valor < 0:
            raise EntradaInvalidaError(
                f"Los datos son inconsistentes: '{nombre}' tira el valor {valor} "
                f"(no puede ser negativo). Revisá las cardinalidades e intersecciones."
            )

    en_alguno = solo_a + solo_b + solo_c + solo_ab + solo_ac + solo_bc + abc
    pasos.append(
        f"Al menos en uno: {solo_a} + {solo_b} + {solo_c} + {solo_ab} + "
        f"{solo_ac} + {solo_bc} + {abc} = {en_alguno}"
    )

    ninguno = u - en_alguno
    pasos.append(f"Ninguno: {u} - {en_alguno} = {ninguno}")

    if ninguno < 0:
        raise EntradaInvalidaError(
            f"Los datos son inconsistentes: la union da {en_alguno}, "
            f"que supera a |U|={u}. Revisá los valores ingresados."
        )

    regiones = RegionesVenn(
        solo_a=solo_a,
        solo_b=solo_b,
        solo_c=solo_c,
        solo_ab=solo_ab,
        solo_ac=solo_ac,
        solo_bc=solo_bc,
        abc=abc,
        ninguno=ninguno,
        en_alguno=en_alguno,
    )
    return regiones, pasos
