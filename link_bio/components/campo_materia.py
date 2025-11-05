import reflex as rx

from link_bio.styles.styles import IconSize, Spacing, Color, button_title_style, Spacing_CSS

# ============================================================
# ESTADO GLOBAL DE LOS ACORDEONES
# ============================================================
class AccordionState(rx.State):
    """
    Estado reactivo compartido por todos los acordeones.
    
    En Reflex, las clases que heredan de rx.State definen "variables reactivas".
    Estas variables pueden ser leídas desde el frontend (como si fueran globales)
    y modificadas mediante eventos del servidor (funciones decoradas con @rx.event).

    Aquí definimos un diccionario que guardará, para cada título de materia,
    si su acordeón está abierto (True) o cerrado (False).
    """
    open_items: dict[str, bool] = {}

    @rx.event
    def toggle(self, key: str):
        """
        Cambia el estado de apertura del acordeón correspondiente.

        Cada vez que el usuario hace clic en un acordeón, este evento se ejecuta
        en el servidor (Reflex sincroniza automáticamente el cambio con el cliente).

        - Si el acordeón estaba cerrado, se marca como abierto.
        - Si estaba abierto, se marca como cerrado.
        """
        current = self.open_items.get(key, False)
        self.open_items[key] = not current

        # Mensaje opcional para depurar en consola del servidor.
        # print(f"[AccordionState] {key}: {'abierto' if self.open_items[key] else 'cerrado'}")
        #print("Estado global actual:", self.open_items)


# ============================================================
# COMPONENTE: BLOQUE DE MATERIA (ACORDEÓN)
# ============================================================
def campo_materia(title: str, imagen_tema: str, temas: list[rx.Component] | None = None) -> rx.Component:
    """
    Crea un bloque de acordeón con un título, un icono y una lista de temas.

    Parámetros:
        - title: nombre del acordeón (p. ej. "Ingeniería de características")
        - imagen_tema: ruta del icono asociado a la materia
        - temas: lista opcional de componentes internos (los contenidos del acordeón)
    """
    return rx.accordion.root(
        # Un acordeón puede tener varios "items" dentro del root.
        rx.accordion.item(
            # ---------- Cabecera (trigger) ----------
            rx.accordion.trigger(
                rx.hstack(
                    # --- Bloque izquierdo (icono + título) ---
                    rx.hstack(
                        # Imagen o icono del tema
                        rx.image(
                            src=imagen_tema,
                            width=IconSize.MD.value,
                            height=IconSize.MD.value,
                            alt=f"Ícono de {title}",
                        ),
                        # Texto del título del acordeón
                        rx.text(
                            title,
                            **button_title_style,  # estilo importado desde tu módulo de estilos
                        ),
                        spacing=Spacing.SM.value,
                        align="center",
                        padding_right=Spacing_CSS.ZERO.value,
                    ),

                    # --- Bloque derecho: icono dinámico ---
                    # Solo usamos un "chevron-down" y lo rotamos cuando se abre.
                    rx.icon(
                        tag="chevron-down",
                        width=IconSize.MD.value,
                        height=IconSize.MD.value,
                        color=Color.DARK.value,
                        # Aquí es donde ocurre la "magia reactiva"
                        style={
                            # Animación suave al rotar
                            "transition": "transform 0.25s ease",
                            # Si el acordeón está abierto → gira 180º (chevron hacia arriba)
                            # Si está cerrado → 0º (chevron hacia abajo)
                            "transform": rx.cond(
                                AccordionState.open_items.get(title) == True,
                                "rotate(180deg)",
                                "rotate(0deg)",
                            ),
                        },
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                ),
                color_scheme="indigo",
            ),
            # ---------- Contenido desplegable ----------
            rx.accordion.content(
                rx.vstack(
                    # Si se pasan temas, los muestra. Si no, muestra un mensaje genérico.
                    *temas if temas else [rx.text("En construcción")],
                    spacing=Spacing.SM.value,
                    width="100%",
                    align="start",
                ),
            ),
        ),

        # ---------- Lógica del acordeón ----------
        # Este evento se dispara cada vez que el usuario abre/cierra el acordeón.
        # Llama a nuestro método toggle() con el título como identificador único.
        on_value_change=lambda _: AccordionState.toggle(title),

        collapsible=True,

        width="100%",
    )


# ============================================================
# RESUMEN DIDÁCTICO
# ============================================================
# Reflex maneja el estado de forma declarativa:
#    - Cada vez que una variable reactiva cambia, Reflex re-renderiza automáticamente
#      las partes del frontend que dependen de ella.
#
# El ciclo completo de interacción:
#    1. El usuario hace clic → `on_value_change` dispara `AccordionState.toggle(title)`
#    2. El servidor actualiza el estado `open_items`
#    3. Reflex envía el nuevo estado al cliente
#    4. El condicional `rx.cond(...)` se evalúa de nuevo → cambia el estilo `transform`
#    5. El icono rota visualmente gracias a la transición CSS
#
# Ventajas:
#    - No se gestionan manualmente clases CSS ni JS.
#    - Todo se mantiene sincrónico entre servidor y frontend.
#    - El patrón es extensible: puedes añadir más propiedades al estado global.
#
# Consejo:
#    Si el acordeón pertenece a un componente independiente (no global),
#    puedes mover el estado dentro de una subclase de `rx.State` específica para él.
#
# ============================================================


##EJEMPLO DE CAMBIO DE ICONOS.

## Estado global para todos los acordeones
#class AccordionState(rx.State): # Clase que el estado reactivo que maneja reflex. Sus atributos son VARIABLES REACTIVAS no objetos python.
#    """Estado global de los acordeones."""
#    icons: dict[str, str] = {}
#
#    @rx.event # Evento: Funcion que se ejecuta en el server
#    def toggle(self, key: str):
#        """Cambia el icono del acordeón correspondiente."""
#        current = self.icons.get(key, "chevron-down")
#        self.icons[key] = "chevron-up" if current == "chevron-down" else "chevron-down"
#
#        
#        
#def campo_materia(title: str, imagen_tema: str, temas: list[rx.Component] | None = None) -> rx.Component:
#    """Crea un bloque de acordeón para una materia."""
#    return rx.accordion.root(
#        rx.accordion.item(
#            rx.accordion.trigger(
#                rx.hstack(
#                    # Bloque izquierdo
#                    rx.hstack(
#                        rx.image(
#                            src=imagen_tema,
#                            width= IconSize.MD.value,
#                            height= IconSize.MD.value,
#                            alt = "Ícono de " + title,
#                        ),
#                        rx.text(title,
#                                **button_title_style),
#                        spacing= Spacing.SM.value,
#                        align="center",
#                        padding_right = Spacing_CSS.ZERO.value, # Añadido por responsive
#                    ),
#                    # Bloque derecho: icono dinámico
#                    rx.icon(
#                        tag=rx.cond(
#                            AccordionState.icons[title] == "chevron-up",
#                            "chevron-up",
#                            "chevron-down"
#                        ),
#                        width = IconSize.MD.value,
#                        height = IconSize.MD.value,
#                        color = Color.DARK.value,
#                    ),
#                    justify="between",
#                    align="center",
#                    width="100%",
#                ),
#                color_scheme="indigo",
#            ),
#            rx.accordion.content(
#                rx.vstack(
#                    *temas if temas else [rx.text("En construcción")],
#                    spacing = Spacing.SM.value,
#                    width="100%",
#                    align="start",
#                ),
#            ),
#        ),
#        on_value_change=lambda _: AccordionState.toggle(title),
#        collapsible=True,
#        width="100%",
#    )