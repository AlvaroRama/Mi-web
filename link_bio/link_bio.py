import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
from link_bio.views.materias.materias import materias
import link_bio.styles.styles as styles
from link_bio.styles.styles import Spacing as Spacing


class State(rx.State):
    """
    Clase que define el estado de la aplicación.
    Puedes definir variables y métodos aquí para manejar el estado.
    """
    # Ejemplo de variable de estado
    pass

"""Defines la función de página llamada index. 
- Cada página en Reflex es una función que devuelve componentes """

# link_bio/link_bio.py (Añadir al inicio)

# Definición de la URL de las fuentes de Google
# Combinamos ambas fuentes en una sola petición para optimizar la carga
# GOOGLE_FONTS_URL = "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&family=Press+Start+2P&display=swap"

GOOGLE_FONTS_URL = "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&family=Silkscreen&display=swap"


def index() -> rx.Component:
    return rx.flex(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                materias(),
                links(),
                max_width = styles.MAX_WIDTH,  # Ancho máximo del contenedor
                width = "100%",
                margin_y = Spacing.XL.value,  # Espacio vertical entre bloques
            )
        ),
        footer(),
    direction = "column",
    spacing = Spacing.BASE.value
    )
        #align="center",   # alinear horizontalmente
        #justify="center", # alinear verticalmente
        #spacing="2em",    # espacio entre bloques
        #width="100%"      # ocupar todo el anch

 # Llama al componente de la barra de navegación
    

"""Creas la aplicación de Reflex. Este objeto coordina:
- El registro de páginas y rutas
- La compilación del frontend (Next.js/React) y el backend (FastAPI)
- La configuración global (tema, estilos, etc., si quisieras añadirla)"""

app = rx.App(
    style = styles.BASE_STYLE,
    # Carga directa de la URL de Google Fonts.
    stylesheets = [GOOGLE_FONTS_URL]
)

"""Registras la página index en la aplicación.

Al no indicar route, Reflex la pone en la ruta raíz /.

El nombre de la función se usa para el título por defecto.

"""
app.add_page(index)


# Compilar la aplicación para generar el frontend

app._compile()