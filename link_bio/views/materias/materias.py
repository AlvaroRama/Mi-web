import reflex as rx

from link_bio.components.tittle import tittle

from link_bio.components.campo_materia import campo_materia

from link_bio.components.link_temas import link_temas

from link_bio.styles.styles import Spacing

def materias() -> rx.Component:
    return rx.vstack(
        tittle("Recursos"),
        campo_materia("Ingeniería de características",
                      "icons/hammer-solid.svg",
                      temas=[
                        link_temas("Selección de variables", "/tema1"),
                        link_temas("Codificación categórica","/tema2"),
                        link_temas("Normalización y escalado", "/tema3"),
                        ],
        ),
        width="100%",
        spacing=Spacing.MD.value
    )