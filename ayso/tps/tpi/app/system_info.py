import os
import socket
from pathlib import Path


def leer_meminfo() -> dict[str, int]:
    valores: dict[str, int] = {}
    meminfo = Path("/proc/meminfo")
    if not meminfo.exists():
        return valores

    for linea in meminfo.read_text(encoding="utf-8").splitlines():
        partes = linea.split(":")
        if len(partes) != 2:
            continue
        clave = partes[0].strip()
        numero = partes[1].strip().split()[0]
        if numero.isdigit():
            valores[clave] = int(numero)
    return valores


def contar_procesos() -> int:
    proc = Path("/proc")
    if not proc.exists():
        return 0
    return sum(1 for entry in proc.iterdir() if entry.name.isdigit())


def leer_cpu_modelo() -> str:
    cpuinfo = Path("/proc/cpuinfo")
    if not cpuinfo.exists():
        return "No disponible"

    for linea in cpuinfo.read_text(encoding="utf-8").splitlines():
        if linea.lower().startswith("model name"):
            return linea.split(":", 1)[1].strip()
    return "No disponible"


def obtener_info_sistema() -> dict:
    memoria = leer_meminfo()
    hostname = socket.gethostname()
    return {
        "hostname": hostname,
        "contenedor_id": os.environ.get("HOSTNAME", hostname),
        "sistema_operativo": os.uname().sysname,
        "kernel": os.uname().release,
        "arquitectura": os.uname().machine,
        "cpu_modelo": leer_cpu_modelo(),
        "memoria_total_kb": memoria.get("MemTotal", 0),
        "memoria_libre_kb": memoria.get("MemAvailable", memoria.get("MemFree", 0)),
        "procesos_activos": contar_procesos(),
        "directorio_trabajo": str(Path.cwd()),
    }
