import reflex as rx
from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.data import Data
from portafolio.styles.styles import Size


def header(data: Data) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src=data.avatar,
            size="9"
        ),
        rx.vstack(
            heading(data.name, True),
            heading(data.skill),
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display="inherit",
            ),
            media(data.media),
            spacing="3",
        ),
        spacing=Size.MEDIUM.value,
    )
