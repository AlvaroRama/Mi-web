import reflex as rx
import link_bio.styles.styles as styles

def link_icon(url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="linkedin",
            width=styles.IconSize.MD.value,
            height=styles.IconSize.MD.value,
            color="white", 
        ),
        href = url,
        is_external = True
    )
    
def github_icon(url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="github",
            width=styles.IconSize.MD.value,
            height=styles.IconSize.MD.value,
            color="white", 
        ),
        href = url,
        is_external = True
    )
    
def kaggle_icon(url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="brain-circuit",
            width=styles.IconSize.MD.value,
            height=styles.IconSize.MD.value,
            color="white", 
        ),
        href = url,
        is_external = True
    )