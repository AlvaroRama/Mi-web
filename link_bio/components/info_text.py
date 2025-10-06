import reflex as rx
from link_bio.styles.styles import TextSize as TextSize
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(title,
                as_="span",
                font_weight="bold",
                color= Color.PURPLE.value),
        f" {body}",
        font_size=TextSize.BASE.value,
        color = TextColor.LIGHT.value
    )