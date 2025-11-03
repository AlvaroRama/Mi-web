import reflex as rx

from link_bio.styles.styles import BASE_STYLE, STYLESHEETS

from link_bio.pages.index import index


class State(rx.State):
    """
    Clase que define el estado de la aplicación.
    Puedes definir variables y métodos aquí para manejar el estado.
    """
    # Ejemplo de variable de estado
    pass



"""Creas la aplicación de Reflex. Este objeto coordina:
- El registro de páginas y rutas
- La compilación del frontend (Next.js/React) y el backend (FastAPI)
- La configuración global (tema, estilos, etc., si quisieras añadirla)"""


# Sustituye "G-XXXXXXXXXX" por tu ID de Google Tag Manager cuando lo tengas
GA_TAG_ID = "G-XXXXXXXXXX" #PENDIENTE TAG Y METERLO COMO VARIABLE DE ENTORNO

app = rx.App(
    stylesheets = STYLESHEETS,
    style = BASE_STYLE,
    head_components=[
        rx.script(src=f"https://www.googletagmanager.com/gtag/js?id={GA_TAG_ID}"),
        rx.script(
            f"""
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{GA_TAG_ID}');
            """
        ),
    ],
)




#--------------REFACTOR--------------------

#"""Defines la función de página llamada index. 
#- Cada página en Reflex es una función que devuelve componentes """
#
#def index() -> rx.Component:
#    return rx.flex(
#        rx.script("document.documentElement.lang='es'"),
#        navbar(),
#        rx.container(
#            rx.center(
#                rx.vstack(
#                    header(),
#                    materias(),
#                    links(),
#                    max_width = MAX_WIDTH,  # Ancho máximo del contenedor
#                ),
#                margin_y = Spacing_CSS.BASE.value
#            ),
#            footer(),
#            direction = "column",
#        ),
#        direction = "column",
#        stack_children_full_width = True
#    )

"""Registras la página index en la aplicación.

Al no indicar router, Reflex la pone en la ruta raíz /.

El nombre de la función se usa para el título por defecto.

"""
#title = "Alvaro Rama Benedicto | Mi web en Reflex con recursos"
#description = "Hola, mi nombre es Álvaro. Bienvenido a esta página donde espero encuentres recursos interesantes relacionados con la ciencia de datos"
#preview = "icons/hammer-solid.svg"
#
#app.add_page(
#    index,    
#    title = title,
#    description = description,
#    image = preview,
#    meta = [
#        {"name": "og:type","content": "website"},
#        {"name": "og:title","content": title},
#        {"name": "og:description","content": description},
#        { "name": "og:image", "content": preview}
#    ]
#)



# Compilar la aplicación para generar el frontend

# app._compile()