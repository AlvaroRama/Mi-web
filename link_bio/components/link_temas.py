import reflex as rx

from typing import Optional

from link_bio.styles.colors import Color as Color

from link_bio.styles.styles import Spacing, IconSize, button_body_style


def link_temas(tittle: str, url: str) -> rx.Component:
    return rx.hstack(
            rx.image(src ="icons/chevron-right-solid.svg",
                width=IconSize.SM.value,
                height=IconSize.SM.value,
                alt= "Icono de flecha derecha",
            ),
            rx.link(
                rx.text(tittle,
                    **button_body_style,
                    _hover = {"color": Color.LIGHT.value},
                ),
                href = url,
                is_external = False
            ),
            spacing= Spacing.XS.value,
            width = "100%",
            justify = "start",
            align="center", # Alinear icono y texto verticalmente
        )
    
    

#def link_temas(tittle: str, url: str) -> rx.Component:
#    return rx.link(
#            rx.hstack(
#                rx.spacer(),
#                rx.image(src = "icons/chevron-right-solid.svg",
#                         width=styles.IconSize.SM.value,
#                         height=styles.IconSize.SM.value
#                         ),
#              
#                rx.text(tittle,
#                            **button_body_style,
#                        ),
#            spacing= Spacing.MD.value,
#            width = "100%",
#            justify = "start",
#            margin = Spacing.ZERO.value,
#            # align="center", # Alinear icono y texto verticalmente
#        ),
#        href = url,
#        is_external = True,
#        width = "100%",  
#    )