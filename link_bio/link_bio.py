import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


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
                links(),
                links(),
                max_width = styles.MAX_WIDTH,  # Ancho máximo del contenedor
                width = "100%",
                margin_y = Size.BIG.value,  # Espacio vertical entre bloques
            )
        ),
        footer(),
    direction = "column",
    spacing = Size.DEFAULT.value
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
    style = styles.BASE_STYLE,  # Estilos globales definidos en styles.py
)

"""Registras la página index en la aplicación.

Al no indicar route, Reflex la pone en la ruta raíz /.

El nombre de la función se usa para el título por defecto.

"""
app.add_page(index)


# Compilar la aplicación para generar el frontend

app._compile()