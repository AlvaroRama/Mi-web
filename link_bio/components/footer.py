import reflex as rx

import datetime

from link_bio.styles.styles import Spacing, ImageSize

def footer() -> rx.Component:
    return rx.vstack(
            rx.text("Web realizada con tecnología Reflex",
                trim="both"
            ),
            rx.link(
                rx.image(src = "favicon.ico",
                        style={"margin": "0 auto",
                                "display": "block"},# Imagen centrada en el footer por css. Patron para centrar imagenes.
                        width = ImageSize.MINI.value,
                        height = ImageSize.MINI.value
                ),
                href="https://reflex.dev/",
                is_external = True,
            ),
            rx.link(
                f"© 2024-{datetime.date.today().year} Álvaro Rama Benedicto",
                href = "https://www.linkedin.com/in/alvaro-rama-benedicto-538603b4/?originalSubdomain=es",
                is_external = True
                # No descubro porqué el link sale en azul si en styles.py he puesto que no tuviera decoración y no cambiara de color al pasar el ratón por encima?      
            ),
            align= "center",      
        )
