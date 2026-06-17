"""
Trabajo Practico Integrador - datos de paises.

Lee y modifica paises.csv (nombre, poblacion, superficie, continente).
Fuentes del dataset: ver FUENTES.md
"""

import csv
from pathlib import Path

CSV_FILE = Path(__file__).parent / "paises.csv"
VALID_CONTINENTS = ("África", "América", "Asia", "Europa", "Oceanía", "Antártida")
FIELDS = ("nombre", "poblacion", "superficie", "continente")


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------


def load_countries() -> list[dict]:
    """Lee el CSV y te devuelve los valores"""
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"No encontré el archivo {CSV_FILE.name}")

    countries = []
    try:
        with CSV_FILE.open(encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if reader.fieldnames != list(FIELDS):
                raise ValueError(
                    "Formato de CSV invalido. Se esperaban las columnas: "
                    + ", ".join(FIELDS)
                )
            for line_number, row in enumerate(reader, start=2):
                try:
                    countries.append(
                        {
                            "nombre": row["nombre"].strip(),
                            "poblacion": int(row["poblacion"]),
                            "superficie": int(row["superficie"]),
                            "continente": row["continente"].strip(),
                        }
                    )
                except (KeyError, ValueError) as error:
                    raise ValueError(
                        f"Error en la linea {line_number} del CSV: {error}"
                    ) from error
    except csv.Error as error:
        raise ValueError(f"Error al leer el CSV: {error}") from error

    return countries


def save_countries(countries: list[dict]) -> None:
    """Esto escribe el pais que cargamos directo al archivo CSV."""
    with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(countries)


# ---------------------------------------------------------------------------
# Input and validation
# ---------------------------------------------------------------------------


def read_text(prompt: str) -> str:
    """Read a non-empty string from the console."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: el campo no puede estar vacio.")


def read_positive_int(prompt: str) -> int:
    """Lee un numero int que sea un positivo"""
    while True:
        text = input(prompt).strip()
        if not text:
            print("Error: el campo no puede estar vacio.")
            continue
        try:
            number = int(text)
            if number <= 0:
                print("Error: debe ingresar un numero entero positivo.")
                continue
            return number
        except ValueError:
            print("Error: debe ingresar un numero entero valido.")


def read_continent() -> str:
    """Lee y valida que el nombre del continente no sea inventado."""
    print("Continentes validos:", ", ".join(VALID_CONTINENTS))
    while True:
        continent = input("Continente: ").strip()
        if continent in VALID_CONTINENTS:
            return continent
        print("Error: continente no valido.")


def read_range(min_prompt: str, max_prompt: str) -> tuple[int, int]:
    """Read a numeric range ensuring minimum <= maximum."""
    minimum = read_positive_int(min_prompt)
    maximum = read_positive_int(max_prompt)
    if minimum > maximum:
        print("Error: el minimo no puede ser mayor que el maximo.")
        return read_range(min_prompt, max_prompt)
    return minimum, maximum


def find_country_index(countries: list[dict], name: str) -> int | None:
    """Busca un país por el nombre exacto es case-insensitive."""
    normalized_name = name.casefold()
    for index, country in enumerate(countries):
        if country["nombre"].casefold() == normalized_name:
            return index
    return None


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------


def display_countries(countries: list[dict], title: str = "Paises") -> None:
    """Hace un print de la lista de llos paises"""
    if not countries:
        print("No hay paises para mostrar.")
        return

    # aclaración de sintaxsis acá:
    # :<28
    # : significa despues del valor del key
    # :< || :> alinear de izquierda o derecha
    # 28 puede ser cualquier número es la cantidad de caracteres a hacer de espacio, sirve para alinear la cabecera de la columna con el valor
    print(f"\n--- {title} ({len(countries)}) ---")
    print(f"{'Nombre':<28} {'Poblacion':>14} {'Superficie':>12} {'Continente'}")
    print("-" * 72)
    for country in countries:
        print(
            f"{country['nombre']:<28} "
            f"{country['poblacion']:>14,} "
            f"{country['superficie']:>12,} "
            f"{country['continente']}"
        )
    print()


# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------


def add_country(countries: list[dict]) -> None:
    """Agrega un nuevo país con los campos requeridos."""
    print("\n--- Agregar pais ---")
    name = read_text("Nombre: ")

    if find_country_index(countries, name) is not None:
        print(f"Error: ya existe un pais con el nombre '{name}'.")
        return

    population = read_positive_int("Poblacion: ")
    area = read_positive_int("Superficie (km2): ")
    continent = read_continent()

    countries.append(
        {
            "nombre": name,
            "poblacion": population,
            "superficie": area,
            "continente": continent,
        }
    )
    save_countries(countries)
    print(f"Pais '{name}' agregado correctamente.")


def update_country(countries: list[dict]) -> None:
    """Actualizar propiedades de un pais que existe"""
    print("\n--- Actualizar país ---")
    name = read_text("Nombre del paíss a actualizar: ")
    index = find_country_index(countries, name)

    if index is None:
        print(f"Error: no se encontró el pais '{name}'.")
        return

    country = countries[index]
    print(
        f"Datos actuales -> Poblacion: {country['poblacion']:,}, "
        f"Superficie: {country['superficie']:,} km2"
    )

    new_population = read_positive_int("Nueva poblacion: ")
    new_area = read_positive_int("Nueva superficie (km2): ")

    countries[index]["poblacion"] = new_population
    countries[index]["superficie"] = new_area
    save_countries(countries)
    print(f"Pais '{country['nombre']}' actualizado correctamente.")


def search_country(countries: list[dict]) -> None:
    """Te busca un país por un match parcial o absoluto."""
    print("\n--- Buscar país ---")
    print("1. Coincidencia exacta")
    print("2. Coincidencia parcial")
    option = input("Opcion: ").strip()
    search_term = read_text("Nombre a buscar: ")
    normalized_term = search_term.casefold()

    if option == "1":
        results = [
            c for c in countries if c["nombre"].casefold() == normalized_term
        ]
    elif option == "2":
        results = [
            c for c in countries if normalized_term in c["nombre"].casefold()
        ]
    else:
        print("Error: opción no valida.")
        return

    if not results:
        print(f"No se encontraron paises para '{search_term}'.")
        return

    display_countries(results, "Resultados de búsqueda")


def filter_by_continent(countries: list[dict]) -> None:
    """Filter countries by continent."""
    print("\n--- Filtrar por continente ---")
    continent = read_continent()
    results = [c for c in countries if c["continente"] == continent]

    if not results:
        print(f"No hay paises en el continente '{continent}'.")
        return

    display_countries(results, f"Paises de {continent}")


def filter_by_population(countries: list[dict]) -> None:
    """Te filtra los paises que estén dentro del rango poblacional."""
    print("\n--- Filtrar por rango de poblacion ---")
    minimum, maximum = read_range("Poblacion minima: ", "Poblacion maxima: ")
    results = [
        c for c in countries if minimum <= c["poblacion"] <= maximum
    ]

    if not results:
        print("No hay paises en ese rango de poblacion.")
        return

    display_countries(results, "Filtro por poblacion")


def filter_by_area(countries: list[dict]) -> None:
    """Filtrar los paises por rangos de superficie."""
    print("\n--- Filtrar por rango de superficie ---")
    minimum, maximum = read_range(
        "Superficie minima (km2): ", "Superficie maxima (km2): "
    )
    results = [
        c for c in countries if minimum <= c["superficie"] <= maximum
    ]

    if not results:
        print("No hay paises en ese rango de superficie.")
        return

    display_countries(results, "Filtro por superficie")


def sort_countries(countries: list[dict]) -> None:
    """Organizar y listar los paises segun un ciretrio particular"""
    # Esta funcion tiene varios comentarios ya que puede llegar a resultar medio compleja
    print("\n--- Ordenar paises ---")
    print("1. Nombre")
    print("2. Poblacion")
    print("3. Superficie")
    criterion = input("Criterio: ").strip()

    print("1. Ascendente")
    print("2. Descendente")
    order = input("Orden: ").strip()

    # Basicamente lista las posibilidades de criterios de forma limitada
    criterion_map = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    # Si está fuera de esas opciones entonces lo descarta como invalido
    if criterion not in criterion_map:
        print("Error: criterio no valido.")
        return
    # lo mismo para el orden ascendente o descendente es 1 o 2 no puede ser otra cosa
    if order not in ("1", "2"):
        print("Error: orden no valido.")
        return

    # Se guarda en "field" el criterio por el cual vamos a estar listando
    field = criterion_map[criterion]
    # Si el orden = 2 es descendente de lo contrario ascendente
    descending: bool = (order == "2")

    # Esto hace uso de funciones anonimas
    # Puede parecer dificl de leer inicialmente pero basicamente la logica es la siguiente:
    # sort_key va a ser <nombre de pais> en minusculas y normalizado si el "field" que elegimos antes es = nombre,
    # de lo contrario va a ser poblacion | superficie. Una de dos.
    sort_key = (
        (lambda c: c[field].casefold())
        if field == "nombre"
        else (lambda c: c[field])
    )
    # Esto crea una nueva lista dict usando sort (ordernar) con el "criterio" elegido como key
    sorted_countries = sorted(countries, key=sort_key, reverse=descending)

    direction = "descendente" if descending else "ascendente"
    display_countries(sorted_countries, f"Ordenados por {field} ({direction})")


def show_statistics(countries: list[dict]) -> None:
    """Calcular las estadisticas para cada pais en el csv."""
    if not countries:
        print("No hay datos para calcular estadisticas.")
        return

    print("\n--- Estadisticas ---")

    max_pop = max(countries, key=lambda c: c["poblacion"])
    min_pop = min(countries, key=lambda c: c["poblacion"])
    avg_population = sum(c["poblacion"] for c in countries) / len(countries)

    print(f"Mayor poblacion: {max_pop['nombre']} ({max_pop['poblacion']:,})")
    print(f"Menor poblacion: {min_pop['nombre']} ({min_pop['poblacion']:,})")
    print(f"Promedio de poblacion: {avg_population:,.0f}")

    max_area = max(countries, key=lambda c: c["superficie"])
    min_area = min(countries, key=lambda c: c["superficie"])
    avg_area = sum(c["superficie"] for c in countries) / len(countries)

    print(f"Mayor superficie: {max_area['nombre']} ({max_area['superficie']:,} km2)")
    print(f"Menor superficie: {min_area['nombre']} ({min_area['superficie']:,} km2)")
    print(f"Promedio de superficie: {int(avg_area)} km2")

    count_by_continent: dict[str, int] = {}
    for country in countries:
        continent = country["continente"]
        count_by_continent[continent] = count_by_continent.get(continent, 0) + 1

    print("\nCantidad de paises por continente:")
    for continent in sorted(count_by_continent):
        print(f"  {continent}: {count_by_continent[continent]}")
    print()


def show_sources() -> None:
    """Mostrar als fuentes de la informacion para el usuario."""
    sources_file = Path(__file__).parent / "FUENTES.md"
    print("\n--- Fuentes de datos ---")
    if sources_file.exists():
        print(sources_file.read_text(encoding="utf-8"))
    else:
        print("No se encontro FUENTES.md en la carpeta del proyecto.")


# ---------------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------------


def show_menu() -> None:
    """Hacer print de las opciones disponibles del menu."""
    print("\n========== GESTION DE PAÍSES ==========")
    print("1.  Agregar país")
    print("2.  Actualizar poblacion y superficie")
    print("3.  Buscar pais")
    print("4.  Filtrar por continente")
    print("5.  Filtrar por rango de poblacion")
    print("6.  Filtrar por rango de superficie")
    print("7.  Ordenar paises")
    print("8.  Mostrar las estadisticas")
    print("9.  Mostrar lista de todos los paises")
    print("10. Ver las fuentes de los datos")
    print("0.  Salir")
    print("======================================")


def main() -> None:
    """Punto de entrada para la aplicacin."""
    try:
        countries: list[dict] = load_countries()
    except (FileNotFoundError, ValueError) as error:
        print(f"Error al iniciar: {error}")
        return

    print(f"Se cargaron {len(countries)} paises desde {CSV_FILE.name}.")

    while True:
        show_menu()
        option = input("Seleccione una opcion: ").strip()

        if option == "1":
            add_country(countries)
        elif option == "2":
            update_country(countries)
        elif option == "3":
            search_country(countries)
        elif option == "4":
            filter_by_continent(countries)
        elif option == "5":
            filter_by_population(countries)
        elif option == "6":
            filter_by_area(countries)
        elif option == "7":
            sort_countries(countries)
        elif option == "8":
            show_statistics(countries)
        elif option == "9":
            display_countries(countries, "Todos los paises")
        elif option == "10":
            show_sources()
        elif option == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    main()
