import reflex as rx
from link_bio.components.tittle import tittle
import link_bio.styles.styles as styles


def material_camp(tittle: str,imagen: str) -> rx.Component:
    return rx.hstack(
        rx.image(src = imagen,
            width=styles.IconSize.MD.value,
            height=styles.IconSize.MD.value
        ),
        rx.accordion.root(
            rx.accordion.item(
                header=tittle,
                content="The first accordion item's content"),
        )
        
    )