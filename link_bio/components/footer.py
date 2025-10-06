import reflex as rx
import datetime
from link_bio.styles.styles import TextSize as TextSize
from link_bio.styles.styles import Spacing as Spacing

from link_bio.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.image(src = "nvidia-logo-dark-2048x2048-9996.jpgo",
                width="40px", height="40px"
                ),
            rx.image(src = "favicon.ico",
                width="40px", height="40px",
                # style={"margin": "0 auto", "display": "block"} # Imagen centrada en el footer por css. Patron para centrar imagenes.
                ),
            rx.image(src = "scikit-learn-logo-small.png",
                width="40px", height="40px"
                )
        ),
        rx.link(
            f"© 2023-{datetime.date.today().year} Álvaro Rama Benedicto",
            href = "https://www.linkedin.com/in/alvaro-rama-benedicto-538603b4/?originalSubdomain=es",
            is_external = True,
            font_size = TextSize.BASE.value
        ),
        rx.text("© 2023 Álvaro Rama Benedicto",
                font_size = TextSize.BASE.value
        ),
        margin_buttom = Spacing.LG.value,
        align="center",
        margin_top=Spacing.XL.value,
        color=TextColor.LIGHT.value
    )


#def footer() -> rx.Component:
#    return rx.center(
#        rx.vstack(
#            rx.image(src = "favicon.ico",
#                     width="40px", height="40px",
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