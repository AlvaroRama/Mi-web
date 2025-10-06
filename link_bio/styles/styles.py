# Styles for the Link Bio application
import reflex as rx
from enum import Enum
from .colors import Color
from .colors import TextColor
from .fonts import Font

# Constants
MAX_WIDTH = "560px"

# -----------------------------
# TOKENS OFICIALES DE REFLEX
# -----------------------------
# Reflex / Radix Themes definen escalas de 1 a 9
# para tipografía, espaciado, etc.

# Tamaños de heading y texto (1 = pequeño, 9 = muy grande)
class TextSize(Enum):
    XS = "1"   # Muy pequeño
    SM = "2"
    MD = "3"
    BASE = "4" # Tamaño por defecto
    LG = "5"
    XL = "6"
    XXL = "7"
    XXXL = "8"
    HUGE = "9" # Más grande posible


# Espaciados (márgenes, paddings, gaps)
# También se expresan con tokens 0-9
class Spacing(Enum):
    ZERO = "0"
    XS = "1"
    SM = "2"
    MD = "3"
    BASE = "4"
    LG = "5"
    XL = "6"
    XXL = "7"
    XXXL = "8"
    HUGE = "9"


# -----------------------------
# ESTILOS GLOBALES
# -----------------------------
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.DARK.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Spacing.SM.value,
        "border_radius": Spacing.BASE.value,
        "color": TextColor.LIGHT.value,
        "background_color": Color.PURPLE.value,
        "_hover": {
            "background_color": Color.PRIMARY.value
        },
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}


# -----------------------------
# ESTILOS ESPECÍFICOS
# -----------------------------
button_title_style = dict(
    size=TextSize.BASE.value,
    color=TextColor.LIGHT.value,
    font_family=Font.DEFAULT.value,
)

button_body_style = dict(
    size=TextSize.MD.value,
    color=TextColor.LIGHT.value,
    font_family=Font.DEFAULT.value,
)

tittle_style = dict(
    width="100%",
    padding_top=Spacing.BASE.value,
    color=TextColor.LIGHT.value,
    font_family=Font.DEFAULT.value,
)

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    size=TextSize.HUGE.value,  # usamos token oficial
)

######################################## ANTIGUO, MEZCLA DE CSS Y REFLEX ########################################

## Styles for the Link Bio application
#import reflex as rx
#from enum import Enum
#from .colors import Color as Color
#from .colors import TextColor as TextColor
#from .fonts import Font as Font
#
## Constants for styling
#MAX_WIDTH = "560px"
#
#
## Sizes:
# # Utilizo tamaños proporcionales con _em_ para que se adapten a diferentes pantallas
#class Size(Enum):
#    ZERO  = "0"  # 0em     ≈ 0rem (0px)
#    SMALL   = "2"  # ~0.5em  ≈ 0.5rem (8px)
#    MEDIUM  = "3"  # ~0.8em  ≈ 0.75rem (12px)
#    DEFAULT = "4"  # 1em     ≈ 1rem (16px)
#    BIG     = "6"  # 2em     ≈ 1.5rem (24px)
#    XL      = "8"  # 4em     ≈ 3rem (48px)
#    XXL     = "9" # 6em     ≈ 4rem (64px)
#   # Huge    = "12" # 8em     ≈ 5rem (80px)
#    
#    
## Global Styles: Recordar que se instancian en App()
#
#BASE_STYLE = {
#    "font_family": Font.DEFAULT.value, # Fuente por defecto de la aplicacion
#    "background_color": Color.DARK.value, # Color de fondo de la aplicacion
#    rx.button: { # Todos los botones de la aplicacion cogeran este estilo.
#        "width": "100%",  # Botones ocuparán todo el ancho del contenedor
#        "height": "100%", # Altura fija para los botones
#        "display": "block", # Mostrar los botones como bloques
#        "padding": Size.SMALL.value, # Espacio interno de los botones
#        "border_radius": Size.DEFAULT.value,
#        "color": TextColor.LIGHT.value, # Color del texto
#        "background_color": Color.PURPLE.value,# Bordes redondeados
#        "_hover": {
#            "background_color": Color.PRIMARY.value # Color de fondo al pasar el cursor
#        }
#    },
#    rx.link: { # Todos los enlaces de la aplicacion cogeran este estilo.
#        "text_decoration": "none",# Sin subrayado
#        "_hover": {} # Estilo al pasar el cursor. Lo dejo vacio para que no haga nada
#    }
#}
#
## Estilo propio del botón de enlace.
#
#buttom_title_style = dict(
#   font_size = Size.DEFAULT.value,
#   color = TextColor.LIGHT.value,
#   font_family= Font.DEFAULT.value
#   
#)
#
#buttom_body_style = dict(
#   font_size = Size.MEDIUM.value,
#   color = TextColor.LIGHT.value,
#   font_family= Font.DEFAULT.value
#)
#
## Estilo propio de los titulos.
#
#tittle_style = dict(
#    # size = '9', # No se puede usar size porque es propiedad propia del componente.Estilo VS propiedad
#    width = "100%",
#    padding_top = Size.DEFAULT.value,
#    color = TextColor.LIGHT.value,
#    font_family= Font.DEFAULT.value
#)
#
## Estilo de la navbar:
#
#navbar_title_style = dict(
#    font_family = Font.LOGO.value,
#    font_size = Size.XXL.value,
#)