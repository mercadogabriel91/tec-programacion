"""
Genera paises.csv a partir de fuentes abiertas verificables.

Fuentes:
  - Banco Mundial: poblacion (SP.POP.TOTL) y superficie (AG.SRF.TOTL.K2)
  - mledoze/countries: nombres en espanol y region ONU

Ver FUENTES.md para enlaces, licencias y como citar.
"""

import csv
import json
import urllib.request
from pathlib import Path

# URLs publicas documentadas en FUENTES.md
MLEDOZE_URL = (
    "https://raw.githubusercontent.com/mledoze/countries/master/dist/countries.json"
)
WB_POP_URL = (
    "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL"
    "?format=json&per_page=500&MRV=1"
)
WB_AREA_URL = (
    "https://api.worldbank.org/v2/country/all/indicator/AG.SRF.TOTL.K2"
    "?format=json&per_page=500&MRV=1"
)

CONTINENT_MAP = {
    "Africa": "África",
    "Americas": "América",
    "Asia": "Asia",
    "Europe": "Europa",
    "Oceania": "Oceanía",
    "Antarctic": "Antártida",
}

OUTPUT_PATH = Path(__file__).parent / "paises.csv"


def fetch_json(url: str) -> object:
    """Descargar y parsear el json de la url."""
    with urllib.request.urlopen(url, timeout=60) as response:
        return json.loads(response.read().decode())


def fetch_world_bank_indicator(url: str) -> dict[str, int]:
    """Descarga y parsea el indicador del Banco Mundial indexado por el código ISO3 del país."""
    meta, data = fetch_json(url)
    result: dict[str, int] = {}
    # Basicamente este diccionario guarda los valores de los paises y sus codigos ISO3

    for item in data or []:
        iso3 = item.get("countryiso3code")
        value = item.get("value")
        if not iso3 or len(iso3) != 3 or value is None:
            continue
        result[iso3] = int(value)

    pages = meta.get("pages", 1)
    if pages > 1:
        for page in range(2, pages + 1):
            page_url = f"{url}&page={page}"
            _, extra_data = fetch_json(page_url)
            for item in extra_data or []:
                iso3 = item.get("countryiso3code")
                value = item.get("value")
                if iso3 and len(iso3) == 3 and value is not None:
                    result[iso3] = int(value)

    return result


def spanish_name(country: dict) -> str:
    """Devuelve el nombre comun en español, y si no lo encuentra, devuelve el nombre en ingles."""
    translation = country.get("translations", {}).get("spa", {})
    return translation.get("common") or country["name"]["common"]


def merge_data(
    mledoze: list, population: dict, area: dict
) -> list[dict]:
    """Combina ambas fuentes en registros listos para el CSV."""
    countries = []

    for country in mledoze:
        iso3 = country.get("cca3")
        region = country.get("region")
        pop = population.get(iso3)
        surface = area.get(iso3)

        if not iso3 or not region or pop is None or surface is None:
            continue

        countries.append(
            {
                "nombre": spanish_name(country),
                "poblacion": pop,
                "superficie": surface,
                "continente": CONTINENT_MAP.get(region, region),
            }
        )

    countries.sort(key=lambda c: c["nombre"].lower())
    return countries


def save_csv(countries: list[dict], path: Path) -> None:
    """Escribe la lista de paises derecho al archivo CSV."""
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["nombre", "poblacion", "superficie", "continente"]
        )
        writer.writeheader()
        writer.writerows(countries)


def main() -> None:
    print("Descargando datos de mledoze/countries...")
    mledoze = fetch_json(MLEDOZE_URL)

    print("Descargando poblacion (Banco Mundial)...")
    population = fetch_world_bank_indicator(WB_POP_URL)

    print("Descargando superficie (Banco Mundial)...")
    area = fetch_world_bank_indicator(WB_AREA_URL)

    countries = merge_data(mledoze, population, area)
    save_csv(countries, OUTPUT_PATH)

    print(f"Listo: {len(countries)} paises guardados en {OUTPUT_PATH.name}")
    print("Fuentes documentadas en FUENTES.md")


if __name__ == "__main__":
    main()
