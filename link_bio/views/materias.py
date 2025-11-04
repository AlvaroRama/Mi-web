import reflex as rx

from link_bio.components.tittle import tittle

from link_bio.components.campo_materia import campo_materia

from link_bio.components.link_temas import link_temas

from link_bio.styles.styles import Spacing

from routes import Router as route

def materias() -> rx.Component:
    return rx.vstack(
        tittle("Recursos"),
        campo_materia("Ingeniería de características",
                      "icons/hammer-solid.svg",
                      temas=[
                        link_temas("Selección de variables", route.PUBLICACIONES.value),
                        link_temas("Codificación categórica","/tema2"),
                        link_temas("Normalización y escalado", "/tema3"),
                        ],
        ),
        campo_materia("Manejo y manipulación de datos",
                      "icons/table-solid.svg",
                      temas=[
                        ],
        ),
        width="100%",
        spacing=Spacing.MD.value
    )