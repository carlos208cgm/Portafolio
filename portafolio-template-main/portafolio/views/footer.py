import reflex as rx
from portafolio.components.media import media
from portafolio.data import Media
from portafolio.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.text("Carlos Andres Morales Flores - 2024"),
        media(data),
        spacing=Size.SMALL.value
    )
