import reflex as rx

from typing import Optional

from link_bio.styles.styles import Spacing, IconSize, button_title_style, button_body_style

def link_buttom(tittle: str, url: str, imagen: str, body: Optional[str] = None ) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(src = imagen,
                         width = IconSize.MD.value,
                         height = IconSize.MD.value
                         ),
                rx.vstack(
                    rx.text(tittle,
                            **button_title_style,
                           ),
                    rx.cond(body,
                            rx.text(body,
                                    **button_body_style)
                            ),
                    spacing= Spacing.MD.value,
                    width = "100%",
                    margin = Spacing.ZERO.value
                    
                ),
            align="center", # Alinear icono y texto verticalmente
            )
        ),
        href = url,
        is_external = True,
        width = "100%",  
    )