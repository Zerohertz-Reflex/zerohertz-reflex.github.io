import reflex as rx
from app.templates.template import template


@template(route="/", title="Home")
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.image("./logo.png"),
            rx.heading("⚡️ Zerohertz's Reflex Application ⚡️", align="center"),
            rx.link(
                rx.button("Source Code"),
                href="https://github.com/Zerohertz-Reflex/zerohertz-reflex.github.io",
                is_external=True,
                align="center",
            ),
            align="center",
            justify="center",
            min_height="85vh",
            spacing="9",
        ),
    )
