import reflex as rx

from link_bio.styles.styles import IconSize , Spacing, Color, button_title_style


# Estado global para todos los acordeones
class AccordionState(rx.State): # Clase que el estado reactivo que maneja reflex. Sus atributos son VARIABLES REACTIVAS no objetos python.
    """Estado global de los acordeones."""
    icons: dict[str, str] = {}

    @rx.event # Evento: Funcion que se ejecuta en el server
    def toggle(self, key: str):
        """Cambia el icono del acordeón correspondiente."""
        current = self.icons.get(key, "chevron-down")
        self.icons[key] = "chevron-up" if current == "chevron-down" else "chevron-down"

        
        
def campo_materia(title: str, imagen_tema: str, temas: list[rx.Component] | None = None) -> rx.Component:
    """Crea un bloque de acordeón para una materia."""
    return rx.accordion.root(
        rx.accordion.item(
            rx.accordion.trigger(
                rx.hstack(
                    # Bloque izquierdo
                    rx.hstack(
                        rx.image(
                            src=imagen_tema,
                            width= IconSize.MD.value,
                            height= IconSize.MD.value,
                        ),
                        rx.text(title,
                                **button_title_style),
                        spacing= Spacing.SM.value,
                        align="center",
                    ),
                    # Bloque derecho: icono dinámico
                    rx.icon(
                        tag=rx.cond(
                            AccordionState.icons[title] == "chevron-up",
                            "chevron-up",
                            "chevron-down"
                        ),
                        width = IconSize.MD.value,
                        height = IconSize.MD.value,
                        color = Color.DARK.value,
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                ),
                color_scheme="indigo",
            ),
            rx.accordion.content(
                rx.vstack(
                    *temas if temas else [rx.text("En construcción")],
                    spacing = Spacing.SM.value,
                    width="100%",
                    align="start",
                ),
            ),
        ),
        on_value_change=lambda _: AccordionState.toggle(title),
        collapsible=True,
        width="100%",
    )






















#class AccordionState(rx.State):
#    """The app state."""
#
#    value: str = "chevron-down"
#    item_selected: str = "chevron-up"
#
#    @rx.event
#    def change_value(self, value):
#        self.value = "chevron-up" if self.value == "chevron-down" else "chevron-down"
#        self.item_selected = value
#
#
#def campo_materia(title: str, imagen_tema: str, temas: list[rx.Component] | None = None) -> rx.Component:
#    return rx.accordion.root(
#        rx.accordion.item(
#            rx.accordion.trigger(
#                rx.hstack(
#                    # Bloque izquierdo: imagen + texto
#                    rx.hstack(
#                        rx.image(
#                            src=imagen_tema,
#                            width=styles.IconSize.MD.value,
#                            height=styles.IconSize.MD.value,
#                        ),
#                        rx.text(title, **button_title_style),
#                        spacing=styles.Spacing.SM.value,
#                        align="center",
#                    ),
#                    # Bloque derecho: icono
#                    rx.icon(
#                        tag=AccordionState.value,
#                        width=styles.IconSize.MD.value,
#                        height=styles.IconSize.MD.value,
#                        color=Color.DARK.value,
#                        bold=True,
#                    ),
#                    justify="between",  # ← Esto empuja el icono a la derecha
#                    align="center",
#                    width="100%",
#                ),
#                color_scheme =  "indigo",
#            ),
#            rx.accordion.content(
#                rx.vstack(
#                    *temas if temas else [rx.text("Sin temas aún")],
#                    spacing=styles.Spacing.SM.value,
#                    width="100%",
#                    align="start",
#                ),
#            ),
#        ),
#        value=AccordionState.item_selected,
#        on_value_change=lambda value: AccordionState.change_value(value),
#        collapsible=True,
#        width="100%",
#    )