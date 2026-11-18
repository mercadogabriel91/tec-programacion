"""Genera un diagrama de Venn de 3 conjuntos y lo guarda como una imagen PNG."""

from pathlib import Path

from matplotlib import pyplot as plt
from matplotlib_venn import venn3

from conjuntos import DatosConjuntos, RegionesVenn


def generar_diagrama_venn(
    datos: DatosConjuntos,
    regiones: RegionesVenn,
    ruta_salida: str = "diagrama_venn.png",
) -> Path:
    """Dibuja el Venn con las regiones exclusivas y lo guarda en disco.

    matplotlib-venn espera las 7 regiones en este orden:
    (Abc, aBc, ABc, abC, AbC, aBC, ABC)
    donde la mayuscula indica pertenencia al conjunto.
    """
    subconjuntos = (
        regiones.solo_a,   # A solo
        regiones.solo_b,   # B solo
        regiones.solo_ab,  # A ∩ B (sin C)
        regiones.solo_c,   # C solo
        regiones.solo_ac,  # A ∩ C (sin B)
        regiones.solo_bc,  # B ∩ C (sin A)
        regiones.abc,      # A ∩ B ∩ C
    )

    figura, eje = plt.subplots(figsize=(9, 7))

    diagrama = venn3(
        subsets=subconjuntos,
        set_labels=(
            f"A: {datos.desc_a}",
            f"B: {datos.desc_b}",
            f"C: {datos.desc_c}",
        ),
        ax=eje,
    )

    # Etiquetas mas claras en cada region (si el area existe en el dibujo)
    etiquetas = {
        "100": f"{regiones.solo_a}\nsolo A",
        "010": f"{regiones.solo_b}\nsolo B",
        "001": f"{regiones.solo_c}\nsolo C",
        "110": f"{regiones.solo_ab}\nA∩B excl.",
        "101": f"{regiones.solo_ac}\nA∩C excl.",
        "011": f"{regiones.solo_bc}\nB∩C excl.",
        "111": f"{regiones.abc}\nA∩B∩C",
    }
    for codigo, texto in etiquetas.items():
        label = diagrama.get_label_by_id(codigo) if diagrama else None
        if label is not None:
            label.set_text(texto)
            label.set_fontsize(9)

    eje.set_title(
        f"Diagrama de Venn\nU = {datos.desc_u}  (|U| = {datos.card_u})",
        fontsize=12,
    )

    # Texto fuera de los circulos: elementos que no pertenecen a ninguno
    eje.text(
        0.02,
        0.02,
        f"Ninguno: {regiones.ninguno}",
        transform=eje.transAxes,
        fontsize=11,
        verticalalignment="bottom",
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.8},
    )

    figura.tight_layout()
    destino = Path(ruta_salida)
    figura.savefig(destino, dpi=150)
    plt.close(figura)
    return destino.resolve()
