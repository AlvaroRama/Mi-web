import reflex as rx
from link_bio.styles.styles import TextSize, Spacing, tittle_style

def tittle(text: str) -> rx.Component:
    return rx.heading(
        text,
        **tittle_style,
        size=TextSize.XL.value,      # Token oficial Reflex
    )


######################################## ANTIGUO, MEZCLA DE CSS Y REFLEX ########################################
#import reflex as rx
#import link_bio.styles.styles as styles
#from link_bio.styles.styles import Size as Size
#
#
#def tittle(text: str) -> rx.Component:
#    return rx.heading(
#        text,
#        style = styles.tittle_style,
#        size = Size.XL.value
#        )