# Fuentes de datos

El archivo `paises.csv` incluido en este proyecto se genera a partir de dos fuentes abiertas y verificables. Cualquier persona puede consultar las mismas fuentes y reproducir el dataset ejecutando `generar_datos.py`.

## 1. Banco Mundial (World Bank Open Data)

**Uso en el proyecto:** población y superficie territorial (km²).

| Campo del CSV | Indicador World Bank | Descripción |
|---------------|----------------------|-------------|
| `poblacion`   | `SP.POP.TOTL`        | Población total |
| `superficie`  | `AG.SRF.TOTL.K2`     | Superficie total (km²) |

**Enlaces para verificar:**

- Portal principal: https://data.worldbank.org/
- Indicador población: https://data.worldbank.org/indicator/SP.POP.TOTL
- Indicador superficie: https://api.worldbank.org/v2/country/all/indicator/AG.SRF.TOTL.K2?format=json&MRV=1
- Documentación de la API: https://datahelpdesk.worldbank.org/knowledgebase/articles/889392

---

## 2. mledoze/countries (GitHub)

**Uso en el proyecto:** nombre del país en español y continente (región ONU).

| Campo del CSV | Origen en mledoze | Descripción |
|---------------|-------------------|-------------|
| `nombre`      | `translations.spa.common` | Nombre común en español |
| `continente`  | `region` (mapeado) | Región ONU traducida al español |

**Enlaces para verificar:**

- Repositorio: https://github.com/mledoze/countries
- Dataset JSON: https://raw.githubusercontent.com/mledoze/countries/master/dist/countries.json
- Sitio del proyecto: https://mledoze.github.io/countries/

**Licencia:** [Open Data Commons Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/).

**Fuentes originales del dataset** (según el repositorio): estándares ISO/ONU, CIA World Factbook y registros geográficos públicos.

### Mapeo de continente

| Región ONU (mledoze) | Valor en `paises.csv` |
|----------------------|------------------------|
| Africa               | África                 |
| Americas             | América                |
| Asia                 | Asia                   |
| Europe               | Europa                 |
| Oceania              | Oceanía                |
| Antarctic            | Antártida              |

---

## Reproducir el dataset

Desde la carpeta del proyecto, con conexión a internet:

```bash
python3 generar_datos.py
```

El script descarga los datos de ambas fuentes, los combina por código ISO-3166 alpha-3 y sobrescribe `paises.csv`.
