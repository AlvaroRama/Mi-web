import reflex as rx

from link_bio.styles.styles import IconSize


def link_icon(url: str, image: str) -> rx.Component:
    return rx.link(
        rx.image(
            src = image,
            width = IconSize.MD.value,
            height = IconSize.MD.value,
             
        ),
        href = url,
        is_external = True
    )
