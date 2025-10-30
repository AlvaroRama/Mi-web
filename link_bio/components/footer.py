import reflex as rx

import datetime

from link_bio.styles.styles import Spacing, ImageSize




def footer() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text("Web realizada con tecnología Reflex",
                trim="both"
            ),
            rx.link(
                rx.image(src = "favicon.ico",
                         ImageSize = ImageSize.AVATAR,
                         style={"margin": "0 auto",
                                "display": "block"}# Imagen centrada en el footer por css. Patron para centrar imagenes.
                ),
                href="https://reflex.dev/",
                is_external = True,
            ),
            align= "center",
            justify = "center"
        ),
        # No descubro porqué el link sale en azul si en styles.py he puesto que no tuviera decoración y no cambiara de color al pasar el ratón por encima?
        rx.link(
            f"© 2023-{datetime.date.today().year} Álvaro Rama Benedicto",
            href = "https://www.linkedin.com/in/alvaro-rama-benedicto-538603b4/?originalSubdomain=es",
            is_external = True,
        ),
        margin_buttom = Spacing.LG.value,
        align="center",
        margin_top=Spacing.XL.value
    )


#def footer() -> rx.Component:
#    return rx.center(
#        rx.vstack(
#            rx.image(src = "favicon.ico",
#                     width=ImageSize.AVATAR, height=ImageSize.AVATAR,
#                     # style={"margin": "0 auto", "display": "block"} # Imagen centrada en el footer por css. Patron para centrar imagenes.
#                     ),
#            rx.link(
#                 f"© 2023-{datetime.date.today().year} Álvaro Rama Benedicto",
#                 href = "https://www.linkedin.com/in/alvaro-rama-benedicto-538603b4/?originalSubdomain=es",
#                 is_external = True,
#                 font_size = Size.MEDIUM.value
#            ),
#            rx.text("© 2023 Álvaro Rama Benedicto",
#                    font_size = Size.MEDIUM.value),
#            margin_buttom = Size.BIG.value
#        )
#    )