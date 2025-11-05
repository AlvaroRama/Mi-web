import reflex as rx

import datetime

from link_bio.styles.styles import ImageSize

def footer() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Web realizada con tecnología Reflex",
            trim="both"
        ),
        rx.link(
            rx.image(
                src="favicon.ico",
                style={
                    "margin": "0 auto",
                    "display": "block",  # Centrar imagen
                },
                width=rx.breakpoints(
                    initial=ImageSize.LOGO_MINI.value,  # móvil (pantallas pequeñas)
                    sm=ImageSize.LOGO.value, 
                ),
                height=rx.breakpoints(
                    initial=ImageSize.LOGO_MINI.value,
                    sm=ImageSize.LOGO.value,
                ),
                alt="Reflex Logo",
            ),
            href="https://reflex.dev/",
            is_external=True,
        ),
        rx.link(
            f"© 2024-{datetime.date.today().year} Álvaro Rama Benedicto",
            href="https://www.linkedin.com/in/alvaro-rama-benedicto-538603b4/?originalSubdomain=es",
            is_external=True,
        ),
        align="center",
    )
