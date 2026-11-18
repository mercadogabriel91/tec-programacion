# Diagrama de Venn — 3 conjuntos

Trabajo práctico integrador N2 de Matemática 1.

Programa de consola en Python que, a partir de un universo `U` y tres
conjuntos `A`, `B` y `C`, calcula las regiones exclusivas de un diagrama
de Venn (solo A, solo B, solo C, intersecciones de a pares sin el tercero,
intersección triple y elementos que no pertenecen a ninguno).

Opcionalmente genera un PNG del diagrama con `matplotlib` /
`matplotlib-venn`.

## Situación de ejemplo

- **U** = totalidad de estudiantes del curso de Matemática de la TUP a Distancia
- **A** = estudiantes que utilizan YouTube para estudiar
- **B** = estudiantes que utilizan ChatGPT
- **C** = estudiantes que utilizan Moodle

## Requisitos

- Python 3
- Entorno virtual + dependencias (para el PNG del diagrama):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar

Desde esta carpeta (con el venv activado):

```bash
python main.py
```

Sin activar el venv:

```bash
.venv/bin/python main.py
```

Menú:

```
*******************************************
   DIAGRAMA DE VENN — 3 CONJUNTOS
*******************************************
 1. Calcular regiones del diagrama
 2. Ejemplo: YouTube / ChatGPT / Moodle
 0. Salir
```

- **Opción 1:** pide descripciones, cardinalidades e intersecciones.
- **Opción 2:** corre el ejemplo orientativo con números ya cargados.
- Después de calcular, te pregunta si querés guardar `diagrama_venn.png`.

## Qué calcula

| Región | Fórmula |
|---|---|
| Solo A ∩ B | \|A ∩ B\| − \|A ∩ B ∩ C\| |
| Solo A ∩ C | \|A ∩ C\| − \|A ∩ B ∩ C\| |
| Solo B ∩ C | \|B ∩ C\| − \|A ∩ B ∩ C\| |
| Solo A | \|A\| − solo A∩B − solo A∩C − \|A ∩ B ∩ C\| |
| Solo B | \|B\| − solo A∩B − solo B∩C − \|A ∩ B ∩ C\| |
| Solo C | \|C\| − solo A∩C − solo B∩C − \|A ∩ B ∩ C\| |
| Ninguno | \|U\| − (suma de las 7 regiones) |

## Estructura

- `main.py` — menú e interacción con el usuario
- `conjuntos.py` — validación de datos y cálculo de regiones
- `diagrama.py` — generación del PNG del Venn
- `requirements.txt` — dependencias gráficas
