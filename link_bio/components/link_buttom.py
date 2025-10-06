import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
from link_bio.styles.styles import Size as Size


def link_buttom(tittle: str, body: str, url: str ) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag = "linkedin",
                    width = styles.Size.BIG.value,
                    height = styles.Size.BIG.value,
                    color="black",
                ),
                rx.vstack(
                    rx.text(tittle,
                            style = styles.buttom_title_style,
                            ),
                    rx.text(body,
                            style = styles.buttom_body_style,
                            ),
                    spacing= Size.SMALL.value,
                    width = "100%",
                    justify = "center",
                    margin = Size.ZERO.value
                    
                ),
                align="center", # Alinear icono y texto verticalmente
            )
        ),
        href = url,
        is_external = True,
        width = "100%",
    )