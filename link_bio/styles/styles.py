# Styles for the Link Bio application
import reflex as rx
from enum import Enum
from .colors import Color
from .colors import TextColor
from .fonts import Font, FontWeight


# Constants
MAX_WIDTH = "560px"

# Fuentes:

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;500;700&display=swap"
]

# -----------------------------
# TOKENS OFICIALES DE REFLEX
# -----------------------------
# Reflex / Radix Themes definen escalas de 1 a 9
# para tipografía, espaciado, etc.

# Tamaños de heading y texto (1 = pequeño, 9 = muy grande) # Utilizados: BASE, SM, XL
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
    
class Spacing_CSS(Enum):
    ZERO = "0em"
    XS = "0.25em"
    SM = "0.5em"
    MD = "0.75em"
    BASE = "1em"
    LG = "1.5em"
    XL = "2em"
    XXL = "2.5em"
    XXXL = "3em"
    HUGE = "4em"

class IconSize(Enum):
    SM = "16px"
    MD = "24px"
    LG = "32px"
    XL = "48px"

class ImageSize(Enum):
    AVATAR = "64px"
    THUMBNAIL = "128px"
    HERO = "100%"


# -----------------------------
# ESTILOS GLOBALES
# -----------------------------
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.DARK.value,
    

    # -----------------------------
    # BOTONES
    # -----------------------------
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Spacing_CSS.SM.value,
        "border_radius": Spacing_CSS.SM.value,
        "color": TextColor.LIGHT.value,
        "background_color": Color.INDIGO.value,
        "_hover": {
            "background_color": Color.INDIGO.value,
        },
    },

    # -----------------------------
    # ACORDEONES
    # -----------------------------
    # Contenedor general del acordeón
    rx.accordion.item: {
        "width": "100%",
        "border_radius": Spacing_CSS.SM.value,
        "background_color": Color.INDIGO.value,
        "overflow": "hidden",  # evita que sobresalga el borde al expandir
    },

    # Trigger (la parte clicable, equivalente al botón)
    rx.accordion.trigger: {
        #"width": "100%",
        "padding": Spacing_CSS.SM.value,
        "display": "flex",
        #"align_items": "left", No parece tener efecto.
        #"gap": Spacing.XXXL.value, No parece tener efecto
        "background_color": Color.INDIGO.value,
        "border_radius": Spacing_CSS.SM.value,
        "cursor": "pointer",
    },

    # Contenido expandido del acordeón
    rx.accordion.content: {
    "padding_top": Spacing_CSS.ZERO.value,
    "padding_right": Spacing_CSS.XS.value,
    "padding_bottom": Spacing_CSS.XS.value,
    "padding_left": Spacing_CSS.XL.value,
    "background_color": Color.INDIGO.value, 
    "color": TextColor.LIGHT.value,
},

    # -----------------------------
    # ENLACES
    # -----------------------------
    rx.link: {
        "text_decoration": "none",
        "_hover": {},
    },
}



# -----------------------------
# ESTILOS ESPECÍFICOS
# -----------------------------

texto_base_style = dict(
    size=TextSize.BASE.value)

heading_style = dict(
    font_weight = FontWeight.MEDIUM.value,
    size=TextSize.XL.value 
)

tittle_style = dict(
    padding_top=Spacing.BASE.value,
    font_family=Font.DEFAULT.value,
    font_weight = FontWeight.MEDIUM.value,
    size=TextSize.XL.value
)

button_title_style = dict(
    color=TextColor.DARK.value,
    font_family=Font.DEFAULT.value,
    font_weight = FontWeight.MEDIUM.value,
    size=TextSize.LG.value
)

button_body_style = dict(
    color=TextColor.DARK.value,
    font_family=Font.DEFAULT.value,
    font_weight = FontWeight.MEDIUM.value,
    size=TextSize.BASE.value
)

navbar_title_style = dict(
    font_family = Font.DEFAULT.value,
    font_weight = FontWeight.HIGHT.value,
    color = Color.LIGHT.value,
    size = TextSize.XL.value
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
#        "background_color": Color.INDIGO.value,# Bordes redondeados
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

#Modificacion despues de añadir el acordeon:
#BASE_STYLE = {
#    "font_family": Font.DEFAULT.value,
#    "background_color": Color.DARK.value,
#    rx.button: {
#        "width": "100%",
#        "height": "100%",
#        "display": "block",
#        "padding": Spacing.SM.value,
#        "border_radius": Spacing.BASE.value,
#        "color": TextColor.LIGHT.value,
#        "background_color": Color.INDIGO.value,
#        "_hover": {
#            "background_color": Color.YELLOW.value
#        },
#    
#    },
#    rx.accordion.item: {     # 🔹 estilo base para los acordeones
#        "width": "100%",
#        "padding": Spacing.SM.value,
#        "border_radius": Spacing.BASE.value,
#        "color": TextColor.LIGHT.value,
#        "background_color": Color.INDIGO.value,
#        "_hover": {}
#    },
#    rx.link: {
#        "text_decoration": "none",
#        "_hover": {}
#    }
#}