# Trabajo Práctico Integrador — Gestión de Datos de Países

Aplicación de consola en Python 3 para gestionar información de países: altas, actualizaciones, búsquedas, filtros, ordenamientos y estadísticas.

## Participantes
Gabriel Emiliano Mercado

## Requisitos

- Python 3.10 o superior
- Archivo `paises.csv` en la misma carpeta

## Uso

```bash
cd programacion-1/trabajo-practico-integrador
python3 tp-integrador.py
```

### Regenerar el dataset desde las fuentes

Requiere conexión a internet:

```bash
python3 generar_datos.py
```

### URLs adicionales: 
1. **Video explicando** — https://youtu.be/-xfSo7MxmzY

## Estructura del proyecto

| Archivo | Descripción |
|---------|-------------|
| `tp-integrador.py` | Programa principal con menú de consola |
| `paises.csv` | Dataset base (nombre, población, superficie, continente) |
| `generar_datos.py` | Script para reproducir `paises.csv` desde las fuentes |
| `FUENTES.md` | Enlaces, licencias y citas bibliográficas |

## Fuentes de datos

Los datos provienen de dos fuentes abiertas y verificables:

1. **Banco Mundial** — población y superficie  
   https://data.worldbank.org/

2. **mledoze/countries** — nombres en español y continente  
   https://github.com/mledoze/countries

Detalle completo, enlaces directos a cada indicador y ejemplos de cita en [`FUENTES.md`](FUENTES.md).

## Formato del CSV

```csv
nombre,poblacion,superficie,continente
Argentina,45696159,2780400,América
Japón,123975371,377969,Asia
```

## Ejemplo de salida (estadísticas)

```
--- Estadisticas ---
Mayor poblacion: India (1,438,069,596)
Menor poblacion: ...
Promedio de poblacion: ...
...
Cantidad de paises por continente:
  África: ...
  América: ...
```
