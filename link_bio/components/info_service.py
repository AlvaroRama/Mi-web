import reflex as rx
from link_bio.styles.colors import Color
from link_bio.styles.styles import TextSize

from rxconfig import target_api_url
import httpx

from datetime import datetime



class Servicios(rx.State):

    status_railway_color: str = "Red"

    message_at_railway: str = "Error de servicio"
    
    status_vercel_color: str = "Red"

    message_at_vercel: str = "Error de servicio"    

    @rx.event
    async def consulta_estado(self):
        
        endpoint = f"{target_api_url}/railway/state"

        try:

            # Llamamos al endpoint que definimos en FastAPI.

            async with httpx.AsyncClient(timeout=5) as client:

                r = await client.get(endpoint)
            
        except Exception:

            return

        if r.status_code == 200:

            data = r.json()
            
            if data["status"] == "SUCCESS":
                
                self.status_railway_color = "Green"
                
                iso_str = data["updated_at"]  # "2025-11-25T12:01:09.525Z"

                dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
                
                formatted = dt.strftime("%d-%m-%Y %H:%M")

                self.message_at_railway = f"Last deploy: {formatted}"


def tarjeta (background_color :str, texto_titulo: str, estado: str)-> rx.components:
    return  rx.card(
        rx.vstack(
            rx.hstack(
                rx.box(
                    width ="20px",
                    height = "20px",
                    border_radius = "50%",
                    background_color= background_color,
                ),
                rx.text(texto_titulo,
                        size=TextSize.SM.value
                        )
            ),
            rx.text(estado,
                    size=TextSize.XS.value
                    )
        ),
    background_color = Color.DARK.value,
    on_click= Servicios.consulta_estado

    ),

def info_service () -> rx.components:
    return rx.hstack(
        tarjeta (Servicios.status_railway_color,"Backend Status", Servicios.message_at_railway),

        tarjeta (Servicios.status_vercel_color,"Frontend Status", Servicios.message_at_vercel)  
    )
    