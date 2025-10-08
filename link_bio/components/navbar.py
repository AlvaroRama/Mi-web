import reflex as rx
from link_bio.styles.styles import TextSize, Spacing, Color, navbar_title_style
from link_bio.styles.fonts import Font

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text("DATAFORGE", color=Color.LIGHT.value,**navbar_title_style),
        ), 
        position="sticky",
        bg=Color.PRIMARY.value,
        padding_x=Spacing.XL.value,
        padding_y=Spacing.XL.value,
        width="100%",
        top=0,
        z_index=999
    )




######################################### ANTIGUO, MEZCLA DE CSS Y REFLEX ########################################
#import reflex as rx
#import link_bio.styles.styles as styles
#from link_bio.styles.styles import Spacing
#
#def navbar() -> rx.Component:
#    return rx.hstack(
#        rx.box(
#            rx.text("DATA", color=styles.Color.LIGHT.value, as_="span"),
#            rx.text("FORGE", color=styles.Color.PURPLE.value, as_="span"),
#            style=styles.navbar_title_style,
#        ),
#        position="sticky",
#        bg=styles.Color.PRIMARY.value,
#        padding_x=Spacing.XL.value,  # Token oficial
#        padding_y=Spacing.XL.value,
#        width="100%",
#        top=0,
#        z_index=999
#    )
#
#
#
#
#
#
#
#
#
#
#
#
#



######################################## ANTIGUO, MEZCLA DE CSS Y REFLEX ########################################

#import reflex as rx
#from link_bio.styles.styles import Size as Size
#from link_bio.styles.colors import TextColor as TextColor
#from link_bio.styles.colors import Color as Color
#import link_bio.styles.styles as styles
#
#def navbar() -> rx.Component:
#    """
#    Define el componente de la barra de navegación.
#    Contiene enlaces a las diferentes secciones de la aplicación.
#    """
#    return rx.hstack( # Define un contenedor horizontal
#        rx.box(
#            rx.text("DATA", color=Color.LIGHT.value, as_="span"),
#            rx.text("FORGE", color=Color.PURPLE.value, as_="span"),
#            style = styles.navbar_title_style,
#            font_family = "IBM Plex Mono"
#        ),
#        position = "sticky", # Posiciona el contenedor de forma fija al viewport
#        bg = Color.PRIMARY.value, # Color de fondo del contenedor
#        padding_x = Size.XL.value, # Añade un padding de 10px alrededor del contenedor
#        padding_y = Size.XL.value,
#        width="100%",# ← Hace que ocupe todo el ancho de la pantalla
#        top = 0, # Posición en la parte superior del viewport
#        z_index = 999 # Asegura que el contenedor esté por encima de otros elementos
#    )