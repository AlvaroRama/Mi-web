import reflex as rx

import link_bio.styles.styles as styles
from link_bio.styles.styles import Spacing as Spacing


from link_bio.styles.styles import button_title_style as button_title_style



def campo_materia(tittle: str, imagen: str) -> rx.Component:
    return rx.accordion.root(
        rx.accordion.item(
            header=rx.accordion.trigger(  # Trigger correcto con la flecha
                rx.hstack(
                    rx.spacer(),
                    rx.image(
                        src=imagen,
                        width=styles.IconSize.MD.value,
                        height=styles.IconSize.MD.value,
                    ),
                    rx.text(tittle, **button_title_style),
                    spacing=Spacing.MD.value,
                    align="center",
                ),
                justify="start",  # evita centrar el texto
                #width="100%",
                padding_left=Spacing.SM.value,
            ),
            content=rx.accordion.content(
                "The first accordion item's content"
            ),
        ),
        collapsible=True,
        width="100%",
    )