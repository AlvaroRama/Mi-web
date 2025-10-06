import reflex as rx
import link_bio.styles.styles as styles

def link_icon(url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="linkedin",
            width=styles.Size.DEFAULT.value,
            height=styles.Size.DEFAULT.value,
            color="white", 
        ),
        href = url,
        is_external = True
    )