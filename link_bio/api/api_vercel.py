from .api_config import fastapi_app
import httpx
import os
import asyncio
from dotenv import load_dotenv
from datetime import datetime
from typing import Optional, Dict, Any 
from fastapi import HTTPException # Usamos HTTPException para manejar errores de forma nativa en FastAPI

# --- CONFIGURACIÓN DE ENDPOINTS Y ENTORNO ---

# Carga de variables de entorno al inicio del script
load_dotenv('.env.development') 

# Constantes de los Endpoints de Vercel
VERCEL_PROJECT_ENDPOINT = "https://api.vercel.com/v9/projects"
VERCEL_DEPLOYMENT_ENDPOINT = "https://api.vercel.com/v6/deployments" 

def _get_vercel_config() -> Dict[str, Optional[str]]:
    """Función para obtener el token y el ID en el momento de la ejecución."""
    return {
        "API_TOKEN": os.getenv("vercel_API_TOKEN"),
        "PROJECT_ID": os.getenv("vercel_PROJECT_ID")
    }

def _get_headers(token: str) -> Dict[str, str]:
    """Genera los HEADERS usando el token proporcionado."""
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

# --- FUNCIONES AUXILIARES (Llamadas a la API) ---

async def _get_project_metadata(config: Dict[str, Optional[str]]) -> Dict[str, Any]:
    """Consulta la metadata del proyecto (incluye updatedAt en milisegundos)."""
    headers = _get_headers(config["API_TOKEN"])
    project_url = f"{VERCEL_PROJECT_ENDPOINT}/{config['PROJECT_ID']}"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(project_url, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            # Devolvemos el timestamp crudo (ms)
            return {"updatedAt": data.get("updatedAt")} 
            
        except httpx.HTTPStatusError as e:
            # Captura errores HTTP (4xx, 5xx)
            raise HTTPException(
                status_code=e.response.status_code,
                detail={"error": "API Error (Project Metadata)", "message": e.response.text}
            ) from e
        except httpx.RequestError as e:
            # Captura errores de conexión
            raise HTTPException(
                status_code=503,
                detail={"error": "Connection Error (Project Metadata)", "message": str(e)}
            ) from e

async def _get_deployment_state(config: Dict[str, Optional[str]]) -> Dict[str, str]:
    """Consulta el estado (READY/BUILDING) del Deployment más reciente."""
    headers = _get_headers(config["API_TOKEN"])
    project_id = config["PROJECT_ID"]
    
    # URL de consulta para obtener el deployment más reciente
    deployment_url = f"{VERCEL_DEPLOYMENT_ENDPOINT}?projectId={project_id}&limit=1"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(deployment_url, headers=headers)
            response.raise_for_status()

            data = response.json()
            deployments = data.get("deployments", [])

            if not deployments:
                return {"status": "NO_DEPLOYMENTS"}
            
            # El estado real se encuentra en el campo 'state' del primer (más reciente) deployment
            status = deployments[0].get("state", "UNKNOWN")
            return {"status": status}
            
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=e.response.status_code,
                detail={"error": "API Error (Deployment Status)", "message": e.response.text}
            ) from e
        except httpx.RequestError as e:
            raise HTTPException(
                status_code=503,
                detail={"error": "Connection Error (Deployment Status)", "message": str(e)}
            ) from e


@fastapi_app.get("/vercel/state") 
async def get_vercel_consolidated_status() -> Dict[str, Any]:
    
    # 1. Obtener y validar la configuración
    config = _get_vercel_config()

    if not config["API_TOKEN"]:
        raise HTTPException(status_code=500, detail={"error": "Internal Configuration Error", "message": "API_TOKEN no configurado."})
    if not config["PROJECT_ID"]:
        raise HTTPException(status_code=500, detail={"error": "Internal Configuration Error", "message": "VERCEL_PROJECT_ID no configurado."})
    
    # 2. Llamadas concurrentes
    # Se ejecutan ambas funciones al mismo tiempo para reducir la latencia total.
    metadata_task = _get_project_metadata(config)
    status_task = _get_deployment_state(config)

    try:
        project_details, deployment_status = await asyncio.gather(metadata_task, status_task)
    except HTTPException:
        # Re-lanza cualquier HTTPException capturada por las funciones auxiliares
        raise 
    
    # 3. Consolidar, formatear y devolver los resultados
    updated_at_ms = project_details.get("updatedAt", 0)

    # Formatear el timestamp a fecha legible
    updated_at_formatted = datetime.fromtimestamp(updated_at_ms / 1000).strftime('%Y-%m-%d %H:%M:%S') if updated_at_ms else "N/A"

    final_result = {
        "status": deployment_status.get("status", "N/A"),
        "updatedAt": updated_at_formatted
    }

    return final_result