import reflex as rx
from typing import Optional
import link_bio.styles.styles as styles

from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
from link_bio.styles.styles import Spacing as Spacing
from link_bio.styles.styles import button_title_style as button_title_style
from link_bio.styles.styles import button_body_style as button_body_style


def link_temas(tittle: str, url: str) -> rx.Component:
    return rx.link(
            rx.hstack(
                rx.spacer(),
                rx.image(src = "icons/chevron-right-solid.svg",
                         width=styles.IconSize.SM.value,
                         height=styles.IconSize.SM.value
                         ),
                rx.vstack(
                    rx.text(tittle,
                            **button_body_style,
                           ),
                    spacing= Spacing.MD.value,
                    width = "100%",
                    justify = "center",
                    margin = Spacing.ZERO.value
                ),
            align="center", # Alinear icono y texto verticalmente
        ),
        href = url,
        is_external = True,
        width = "100%",  
    )