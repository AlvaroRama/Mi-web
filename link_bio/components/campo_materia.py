import reflex as rx

import link_bio.styles.styles as styles

from link_bio.styles.styles import Spacing as Spacing

from link_bio.styles.colors import Color as Color

from link_bio.styles.styles import button_title_style as button_title_style

class AccordionState(rx.State):
    """The app state."""

    value: str = "chevron-down"
    item_selected: str = "chevron-up"

    @rx.event
    def change_value(self, value):
        self.value = "chevron-up" if self.value == "chevron-down" else "chevron-down"
        self.item_selected = value


def campo_materia(title: str, imagen_tema: str, temas: list[rx.Component] | None = None) -> rx.Component:
    return rx.accordion.root(
        rx.accordion.item(
            rx.accordion.trigger(
                rx.hstack(
                    # Bloque izquierdo: imagen + texto
                    rx.hstack(
                        rx.image(
                            src=imagen_tema,
                            width=styles.IconSize.MD.value,
                            height=styles.IconSize.MD.value,
                        ),
                        rx.text(title, **button_title_style),
                        spacing=styles.Spacing.SM.value,
                        align="center",
                    ),
                    # Bloque derecho: icono
                    rx.icon(
                        tag=AccordionState.value,
                        width=styles.IconSize.MD.value,
                        height=styles.IconSize.MD.value,
                        color=Color.DARK.value,
                        bold=True,
                    ),
                    justify="between",  # ← Esto empuja el icono a la derecha
                    align="center",
                    width="100%",
                ),
                color_scheme =  "indigo",
            ),
            rx.accordion.content(
                rx.vstack(
                    *temas if temas else [rx.text("Sin temas aún")],
                    spacing=styles.Spacing.SM.value,
                    width="100%",
                    align="start",
                ),
            ),
        ),
        value=AccordionState.item_selected,
        on_value_change=lambda value: AccordionState.change_value(value),
        collapsible=True,
        width="100%",
    )