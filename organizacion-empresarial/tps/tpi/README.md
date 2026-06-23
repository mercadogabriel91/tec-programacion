# TPI — Bot de Vacaciones (Obsidian Systems) es el nombre ficticio de mi empresa ficticia

Chatbot simulador en consola para el Trabajo Práctico Integrador de **Organización Empresarial**. Automatiza solicitudes de vacaciones siguiendo un modelo BPMN 2.0, con PostgreSQL y máquina de estados.

## Requisitos

Antes de empezar, necesitás tener instalado en tu sistema:

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** (incluye Docker Compose)
  - macOS / Windows: instaláte Docker y fijate que ande
  - Linux: Docker Engine + plugin Compose v2.

Comprobar que funciona:

```bash
docker --version
docker compose version
```

## Configuración inicial (solo la primera vez)

```bash
cd organizacion-empresarial/tps/tpi
cp .env.example .env
chmod +x correr_bot.sh
```

El archivo `.env` define credenciales de PostgreSQL y reglas del bot. Los valores por defecto alcanzan para desarrollo local.

## Cómo usar el bot

**Usá el script `correr_bot.sh`.** Levanta PostgreSQL en segundo plano y abre el bot en modo interactivo en tu terminal.

```bash
cd organizacion-empresarial/tps/tpi
./correr_bot.sh
```

Vas a ver el menú y el prompt `> `. Ahí escribís y presionás Enter.

> **No uses `docker compose up` solo** para hablar con el bot: muestra logs pero no conecta tu teclado. El script `correr_bot.sh` ya hace lo correcto.

### Si modificaste `bot/db/seed.sql`

Postgres solo carga el seed cuando la base se crea por primera vez. Para aplicar datos nuevos:

```bash
docker compose down -v
./correr_bot.sh
```

Eso borra la base anterior y la recrea con el seed actualizado.

## Cómo usar el bot

Ejemplo — consultar saldo:

```
> 2
> 1001
> 0
```

Ejemplo — pedir vacaciones:

```
> 1
> 1001
> 07/07/2026
> 09/07/2026
> Descanso
> si
> 0
```

| Entrada | Acción |
|---------|--------|
| `1` | Solicitar vacaciones |
| `2` | Consultar saldo |
| `3` | Ver historial |
| `0` | Salir |
| `menu` / `cancelar` / `ayuda` | Comandos globales |

Fechas en formato `DD/MM/AAAA` (solo días hábiles, lunes a viernes).

## Datos de prueba

| Legajo | Empleado       | Saldo inicial |
|--------|----------------|---------------|
| 1001   | Soledad García | 14            |
| 1002   | Esteban Quito  | 8             |
| 1003   | Valeria Mazda  | 20            |
| 1004   | Diego Sanchez  | 3             |
| 1005   | Elena No       | 10            |

## DBeaver / psql (opcional)

Con la base levantada (`docker compose up -d db` o `./correr_bot.sh`):

| Campo    | Valor (default) |
|----------|-----------------|
| Host     | `localhost`     |
| Puerto   | `5432`          |
| Database | `vacaciones`    |
| Usuario  | `vacaciones`    |
| Password | `vacaciones`    |


## Variables de entorno

Ver [`.env.example`](.env.example).

## Estructura del proyecto

```
correr_bot.sh            → script para levantar DB + bot
docker-compose.yml
bpmn-files               → Archivos bpmn para ver las estructuras
bot/
  main.py                → entrada CLI
  states.py              → máquina de estados (BPMN)
  handlers/conversation.py
  db/                    → schema, seed, queries
```
