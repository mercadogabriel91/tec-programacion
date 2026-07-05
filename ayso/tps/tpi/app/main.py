from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import db
from app.system_info import obtener_info_sistema

app = FastAPI(
    title="Monitor de Sistema Containerizado",
    description="API de demostración para el TPI de virtualización con Docker",
    version="1.0.0",
)

templates = Jinja2Templates(directory="app/templates")


@app.get("/health")
def health():
    db_ok = db.verificar_conexion_db()
    return {
        "estado": "ok" if db_ok else "degradado",
        "base_de_datos": "conectada" if db_ok else "sin conexion",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }


@app.get("/api/info")
def api_info():
    info = obtener_info_sistema()
    consulta_id = db.guardar_consulta(
        hostname=info["hostname"],
        memoria_total_kb=info["memoria_total_kb"],
        memoria_libre_kb=info["memoria_libre_kb"],
        procesos_activos=info["procesos_activos"],
    )
    info["consulta_id"] = consulta_id
    return info


@app.get("/api/historial")
def api_historial(limit: int = 10):
    return {"consultas": db.listar_consultas(limit=limit)}


@app.get("/", response_class=HTMLResponse)
def pagina_principal(request: Request):
    info = obtener_info_sistema()
    historial = db.listar_consultas(limit=5)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"info": info, "historial": historial},
    )
