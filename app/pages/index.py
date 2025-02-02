import reflex as rx
from app.templates.template import template


@template(route="/", title="Home")
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.image("./zerohertz-black-red.png"),
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code("app"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )
