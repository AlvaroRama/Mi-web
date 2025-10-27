import reflex as rx

import link_bio.styles.styles as styles
from link_bio.styles.styles import Spacing as Spacing


from link_bio.styles.styles import button_title_style as button_title_style





def campo_materia(title: str, imagen_tema: str) -> rx.Component:
    return rx.accordion.root(
        rx.accordion.item(
            rx.accordion.trigger(
                rx.hstack(
                    rx.spacer(),
                    rx.image(
                        src=imagen_tema,
                        width=styles.IconSize.MD.value,
                        height=styles.IconSize.MD.value,
                    ),
                    rx.text(title, **button_title_style),
                    rx.flex(
                        rx.icon(
                            "chevron-down",
                            width=styles.IconSize.MD.value,
                            height=styles.IconSize.MD.value,
                            transition="transform 0.2s",
                            _group_open={"transform": "rotate(180deg)"},
                        ), 
                        align="end",
                        justify="end",
                    ),
                    spacing=Spacing.MD.value,
                    align="center",
                ),
                justify="start",
                _group={"display": "flex", "align_items": "center"},
            ),
            rx.accordion.content(
                "The first accordion item's content"
            ),
        ),
        on_value_change=lambda value: rx.console_log(f"Accordion changed to: {value}"),
        collapsible=True,
        width="100%",
    )        