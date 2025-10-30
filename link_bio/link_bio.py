import reflex as rx

from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.views.materias.materias import materias

from link_bio.components.navbar import navbar
from link_bio.components.footer import footer


from link_bio.styles.styles import MAX_WIDTH, Spacing, BASE_STYLE, STYLESHEETS


class State(rx.State):
    """
    Clase que define el estado de la aplicación.
    Puedes definir variables y métodos aquí para manejar el estado.
    """
    # Ejemplo de variable de estado
    pass

"""Defines la función de página llamada index. 
- Cada página en Reflex es una función que devuelve componentes """

def index() -> rx.Component:
    return rx.flex(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                materias(),
                links(),
                max_width = MAX_WIDTH,  # Ancho máximo del contenedor
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
    style = BASE_STYLE,
    # Carga directa de la URL de Google Fonts.
    #stylesheets = [GOOGLE_FONTS_URL]
    stylesheets = STYLESHEETS
)

"""Registras la página index en la aplicación.

Al no indicar route, Reflex la pone en la ruta raíz /.

El nombre de la función se usa para el título por defecto.

"""
app.add_page(
    index,    
    title = "Alvaro Rama Benedicto | Mi web en Reflex con recursos",
    description = "Hola, mi nombre es Álvaro. Bienvenido a esta página donde espero encuentres recursos interesantes relacionados con la ciencia de datos",
    image = "icons/hammer-solid.svg")


# Compilar la aplicación para generar el frontend

app._compile()