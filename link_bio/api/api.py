from fastapi import FastAPI, HTTPException
import httpx

fastapi_app = FastAPI(title="My API")

# Lógica que genera el dato
def hello() -> str:
    return "hola alvaro"

# El endpoint de FastAPI expuesto por api_transformer
@fastapi_app.get("/hello")
async def saludo() -> str:
    return hello()

@fastapi_app.get("/railway/{estado}")
async def estado_railway(estado: str)->bool:
    if estado == "online":
        return True
    return False

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