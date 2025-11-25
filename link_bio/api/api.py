from fastapi import FastAPI

fastapi_app = FastAPI(title="My API")

# Lógica que genera el dato
def hello() -> str:
    return "hola alvaro"

def otra_cosa()->str:
    return "Hola de nuevo"

# El endpoint de FastAPI expuesto por api_transformer
@fastapi_app.get("/hello")
async def saludo() -> str:
    return hello()


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