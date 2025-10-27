import reflex as rx
from link_bio.components.link_buttom import link_buttom
from link_bio.components.tittle import tittle
from link_bio.styles.styles import Spacing
import link_bio.constants as const

def links() -> rx.Component:
    return rx.vstack(
        tittle("Recursos"),
        
        tittle("RRSS"),
        link_buttom("Visita mi perfil de Linkedin",
                    const.LINKEDIN_URL,
                    "icons/linkedin_oscuro.svg"
                    ),
        tittle("Contacto"),
        link_buttom("Para cualquier cosa...escribeme!",
                    f"mailto:{const.GMAIL}",
                    "icons/correo_oscuro.svg"),
        width="100%",
        spacing=Spacing.MD.value
    )



######################################## ANTIGUO, MEZCLA DE CSS Y REFLEX #########################################
#import reflex as rx
#from link_bio.components.link_buttom import link_buttom
#from link_bio.components.tittle import tittle
#from link_bio.styles.styles import Size as Size
#import link_bio.constants as const
#
#def links() -> rx.Component:
#    return rx.vstack(
#        tittle("Comunidad"),
#        link_buttom("Linkedint",
#                    "Ejemplo de body",
#                    const.LINKEDIN_URL),
#        link_buttom("You Tube",
#                    "Ejemplo de body",
#                    const.LINKEDIN_URL),
#        link_buttom("Discord",
#                    "Ejemplo de body",
#                    const.LINKEDIN_URL),
#        link_buttom("Proyectos",
#                    "Ejemplo de body",
#                    const.LINKEDIN_URL),
#        tittle("Contacto"),
#        link_buttom("Contacto",
#                    const.GMAIL,
#                    f"mailto:{const.GMAIL}"),
#        width="100%",
#        spacing = Size.MEDIUM.value
#    )
#