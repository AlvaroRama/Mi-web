import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text

from link_bio.styles.styles import TextSize as TextSize
from link_bio.styles.styles import Spacing as Spacing
from link_bio.styles.styles import heading_style
from link_bio.styles.styles import texto_base_style

from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color

import link_bio.constants as constants

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box("ARB",
                color=Color.LIGHT.value,
                bg=Color.DARK.value,
                font_size=TextSize.SM.value, # Propiedad de CSS en em, no es un token de Reflex.
                width="80px",
                height="80px",
                display="flex",
                align_items="center",
                justify_content="center",
                border="2px solid white",
                text_shadow="1px 1px 0 #fff, -1px -1px 0 #fff, "
                            "1px -1px 0 #fff, -1px 1px 0 #fff",
            ),
            rx.vstack(
                rx.heading(
                    "Álvaro Rama Benedicto",
                    **heading_style,
                    trim="both"
                    
                ),
                rx.text("@alvarorama",
                        size = TextSize.SM.value,
                        # trim="start",  # Elimina espacios al principio
                        align="center",
                        width="100%",               
                ),
                rx.hstack(
                    link_icon(constants.LINKEDIN_URL,"icons/linkedin.svg"),
                    link_icon(constants.LINKEDIN_URL,"icons/github.svg"),
                    link_icon(constants.LINKEDIN_URL,"icons/kaggle.svg"),
                    width="100%",
                    justify="center",
                    spacing = Spacing.HUGE.value
                                      
                ),
                spacing=Spacing.SM.value,
            ),
            align="center",
            width="100%"
            
        ),
        rx.hstack(
            info_text("Python friendly", "center"),
            info_text("ML & MLOPS", "center"),   
            info_text("Estadística práctica", "center"),      
            width="100%",
            justify = "between"
        ),
        rx.text(
            """Desarrollo de aplicaciones basadas en datos con Python y diferentes tecnologías.
                Esta es mi web con publicaciones orientadas al aprendizaje automático.""",
                ),
        align_items = "start"
    )




#
#def header() -> rx.Component:
#    return rx.center(   # este center envuelve TODO el header
#        rx.vstack(
#            rx.hstack(
#                rx.box(
#                    "ARB",
#                    color="white",
#                    bg="black",
#                    font_family="monospace",
#                    font_size="2em",
#                    width="80px",
#                    height="80px",
#                    display="flex",
#                    align_items="center",
#                    justify_content="center",
#                    border="2px solid white",
#                    text_shadow="1px 1px 0 #fff, -1px -1px 0 #fff, "
#                                "1px -1px 0 #fff, -1px 1px 0 #fff",
#                ),
#                rx.vstack(
#                    rx.text("Álvaro Rama Benedicto",
#                            size="4",
#                            ),
#                    rx.text(
#                        "@alvarorama",
#                        size="3",
#                        # line_height="1em", # TEORICAMENTE SEGUN GPT altura de línea para centrar verticalmente. Funciona
#                        trim="both", # Lo mismo que arriva pero según la documentación de Reflex.
#                        align="center", # Importante para la alineacion, tengo que hacer que el contenedor del texto ocupe el 100%.
#                        width="100%",
#                    ),
#                    spacing="0"
#                ),
#                spacing="1",   # espacio horizontal entre box y textos
#            ),
#            rx.text(
#                """Desarrollo software especializado en Python.
#                También trabajamos con diferentes tecnologías.
#                Esta es mi web de link con publicaciones de aprendizaje automático"""
#            ),
#            spacing="1",   # espacio vertical entre bloques
#            align="center",  # centra los hijos en el eje horizontal
#        )
#    )

