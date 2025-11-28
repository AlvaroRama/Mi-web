from fastapi import FastAPI, HTTPException
import httpx

from dotenv import load_dotenv
import os

from datetime import datetime
import json
from starlette.responses import JSONResponse

load_dotenv('.env.development')


fastapi_app = FastAPI(title="My API")

# Lógica que genera el dato
def hello() -> str:
    return "hola alvaro"

# El endpoint de FastAPI expuesto por api_transformer
@fastapi_app.get("/hello")
async def saludo() -> str:
    return hello()



# Estado del backend:

import os
import httpx
from fastapi import HTTPException
from starlette.responses import JSONResponse
import json
from datetime import datetime

# --- 1. CARGA DE VARIABLES DE ENTORNO ---
# Se utiliza os.getenv() según su indicación. Esto debe estar en la parte 
# superior de su script o módulo donde define el endpoint de FastAPI.
API_TOKEN = os.getenv("railway_API_TOKEN")
PROJECT_ID = os.getenv("railway_PROJECT_ID")
ENVIRONMENT_ID = os.getenv("railway_ENVIRONMENT_ID")
SERVICE_ID = os.getenv("railway_SERVICE_ID")

RAILWAY_GRAPHQL_ENDPOINT = "https://backboard.railway.com/graphql/v2"

# --- SU FUNCIÓN FastAPI ---

@fastapi_app.get("/railway/state")
async def estado_railway():
    """
    Consulta el último despliegue de un servicio en la API de Railway.
    Maneja la autenticación y los errores de conexión.
    """
    
    # 2. VERIFICACIÓN CRÍTICA DE VARIABLES DE ENTORNO
    # Si falta alguna variable, devolvemos un error 500 para notificar
    if not all([API_TOKEN, PROJECT_ID, ENVIRONMENT_ID, SERVICE_ID]):
        missing = [name for name, val in [("API_TOKEN", API_TOKEN), ("PROJECT_ID", PROJECT_ID), 
                                          ("ENVIRONMENT_ID", ENVIRONMENT_ID), ("SERVICE_ID", SERVICE_ID)] if not val]
        raise HTTPException(
            status_code=500, 
            detail=f"Faltan variables de entorno necesarias para Railway: {', '.join(missing)}"
        )
        
    # 3. DEFINICIÓN DE LA CONSULTA (usamos f-string para interpolar las variables)
    QUERY = """
    query GetMeInfo {
        me { 
            name 
            email 
        }
    }
    """
    #QUERY = f"""
    #query GetLatestDeploymentInfo {{
    #  deployments(
    #    first: 1 
    #    input: {{
    #      projectId: "{PROJECT_ID}"
    #      environmentId: "{ENVIRONMENT_ID}"
    #      serviceId: "{SERVICE_ID}"
    #    }}
    #  ) {{
    #    edges {{
    #      node {{
    #        status       
    #        createdAt    
    #      }}
    #    }}
    #  }}
    #}}
    #"""

    # 4. PREPARACIÓN DE LA PETICIÓN
    HEADERS = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    PAYLOAD = {"query": QUERY}

    # 5. EJECUCIÓN ASÍNCRONA
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                RAILWAY_GRAPHQL_ENDPOINT, 
                headers=HEADERS, 
                json=PAYLOAD,
                timeout=10.0
            )
            response.raise_for_status() 
            data = response.json()
            
            # Manejo de errores de GraphQL
            if 'errors' in data:
                error_msg = f"Error GraphQL: {json.dumps(data['errors'])}"
                # Devolvemos un 400 Bad Request si la consulta es rechazada por Railway
                raise HTTPException(status_code=400, detail=error_msg)

            # ... [Resto del procesamiento de la respuesta, como en el ejemplo anterior] ...
            deployments_data = data.get('data', {}).get('deployments', {})
            
            if not deployments_data or not deployments_data.get('edges'):
                return JSONResponse(content={"status": "NODATA", "message": "No se encontraron despliegues."}, status_code=200)

            latest_deployment = deployments_data['edges'][0]['node']
            
            return {
                "status": latest_deployment.get('status', 'N/A'),
                "created_at_iso": latest_deployment.get('createdAt', 'N/A'),
                "message": "Información obtenida con éxito."
            }

    except httpx.HTTPStatusError as e:
        # Errores de Railway (ej. 401 si el API_TOKEN es inválido)
        raise HTTPException(status_code=e.response.status_code, detail=f"Error de autenticación o solicitud a Railway: {e.response.text}")
    except Exception as e:
        # Errores de red o internos
        raise HTTPException(status_code=500, detail=f"Error interno/de conexión: {e}")
    




@fastapi_app.get("/github/{username}")
async def github_profile(username: str):

    url = f"https://api.github.com/users/{username}"

    async with httpx.AsyncClient(timeout=5) as client:

        r = await client.get(url)

    if r.status_code != 200:

        raise HTTPException(status_code=404, detail="User not found")

    data = r.json()

    return {

        "url": data.get("html_url"),

        "avatar": data.get("avatar_url"),
    }




#######EJEMPLO DE SINCRONIA##########
#
#import asyncio # Necesario para simular esperas
## 1. Definimos la función con 'async def'
## Esto la convierte en una "Corutina" (una promesa de un valor futuro)
#async def hello_lento() -> str:
#    # Simulamos que tarda 2 segundos en buscar el dato (ej. consulta a BD)
#    await asyncio.sleep(2) 
#    return "hola alvaro (llegué tarde)"
#
## 2. El endpoint también debe ser async para poder esperar (await)
#@fastapi_app.get("/hello")
#async def saludo() -> str:
#    # AQUI SÍ usamos 'await'.
#    # Le decimos: "Pausa esta función hasta que hello_lento termine"
#    resultado = await hello_lento()
#    return resultado