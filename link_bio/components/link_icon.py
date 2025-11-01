import reflex as rx

from link_bio.styles.styles import IconSize


def link_icon(url: str, image: str, image_link: str) -> rx.Component:
    return rx.link(
        rx.image(
            src = image,
            width = IconSize.MD.value,
            height = IconSize.MD.value,
            alt = f"Icono de {image_link}",
             
        ),
        href = url,
        is_external = True
    )
