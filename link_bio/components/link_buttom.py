import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
from link_bio.styles.styles import Spacing as Spacing
from link_bio.styles.styles import button_body_style as button_body_style


def link_buttom(tittle: str, body: str, url: str ) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag = "linkedin",
                    width = styles.Spacing.XL.value,
                    height = styles.Spacing.XL.value,
                    color="black",
                ),
                rx.vstack(
                    rx.text(tittle,
                            style = styles.button_body_style,
                            ),
                    rx.text(body,
                            style = styles.button_body_style,
                            ),
                    spacing= Spacing.MD.value,
                    width = "100%",
                    justify = "center",
                    margin = Spacing.ZERO.value
                    
                ),
                align="center", # Alinear icono y texto verticalmente
            )
        ),
        href = url,
        is_external = True,
        width = "100%",
    )