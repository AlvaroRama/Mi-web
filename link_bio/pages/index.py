import reflex as rx

import link_bio.utils as utils

from link_bio.views.header import header
from link_bio.views.links import links
from link_bio.views.materias import materias

from link_bio.components.navbar import navbar
from link_bio.components.footer import footer

from link_bio.styles.styles import MAX_WIDTH, Spacing_CSS, BASE_STYLE, STYLESHEETS

from link_bio.api.api import hello

#from link_bio.api.api import otra_cosa

class IndexState(rx.State):
    
    mensaje: str = "Hola"
    
    @rx.var
    def say_hello(self)-> str:
        return hello()
        

    
@rx.page(
    title = utils.index_title,
    description = utils.index_description,
    image= utils.preview,
    meta = utils.index_meta,
)

def index() -> rx.Component:
    return rx.flex(
        utils.lang(),
        navbar(),
        rx.container(
            rx.center(
                rx.vstack(
                    header(),
                    materias(),
                    rx.text(IndexState.say_hello),
                    links(),
                    max_width = MAX_WIDTH,  # Ancho máximo del contenedor
                ),
                margin_y = Spacing_CSS.BASE.value
            ),
            footer(),
            direction = "column",
        ),
        direction = "column",
        stack_children_full_width = True
    )