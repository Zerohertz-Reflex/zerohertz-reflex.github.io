import reflex as rx
from app.styles import styles


def menu_item_icon(icon: str) -> rx.Component:
    return rx.icon(icon, size=20)


def menu_item(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.match(
                text,
                ("Home", menu_item_icon("home")),
                ("Awesome JMY", menu_item_icon("graduation-cap")),
                menu_item_icon("layout-dashboard"),
            ),
            rx.text(text, size="4", weight="regular"),
            color=styles.accent_text_color,
            style={
                "_hover": {
                    "background_color": styles.accent_bg_color,
                    "opacity": "1",
                },
                "opacity": "1",
            },
            align="center",
            border_radius=styles.border_radius,
            width="100%",
            spacing="2",
            padding="0.35em",
        ),
        underline="none",
        href=url,
        width="100%",
    )


def navbar_footer() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.icon("github", size=18),
            href="https://github.com/Zerohertz",
            color_scheme="gray",
            underline="none",
            target="_blank",
        ),
        rx.link(
            rx.icon("rss", size=18),
            href="https://zerohertz.github.io/",
            color_scheme="gray",
            underline="none",
            target="_blank",
        ),
        justify="start",
        align="center",
        width="100%",
        padding="0.35em",
    )


def menu_button() -> rx.Component:
    from reflex.page import get_decorated_pages

    ordered_page_routes = [
        "/",
        "/awesome-jmy",
    ]
    pages = get_decorated_pages()
    ordered_pages = sorted(
        pages,
        key=lambda page: (
            ordered_page_routes.index(page["route"])
            if page["route"] in ordered_page_routes
            else len(ordered_page_routes)
        ),
    )
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon("align-justify"),
        ),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.hstack(
                        rx.spacer(),
                        rx.drawer.close(rx.icon(tag="x")),
                        justify="end",
                        width="100%",
                    ),
                    rx.divider(),
                    *[
                        menu_item(
                            text=page.get(
                                "title", page["route"].strip("/").capitalize()
                            ),
                            url=page["route"],
                        )
                        for page in ordered_pages
                        if page["route"].count("/") < 2
                    ],
                    rx.spacer(),
                    navbar_footer(),
                    spacing="4",
                    width="100%",
                ),
                top="auto",
                left="auto",
                height="100%",
                width="20em",
                padding="1em",
                bg=rx.color("gray", 1),
            ),
            width="100%",
        ),
        direction="right",
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.hstack(
            rx.image("/favicon.ico", height="1.5em"),
            rx.spacer(),
            rx.color_mode.button(style={"opacity": "0.8", "scale": "0.95"}),
            menu_button(),
            align="center",
            width="100%",
            padding_y="1.25em",
            padding_x=["1em", "1em", "2em"],
        ),
        display=["block", "block", "block", "block", "block", "block"],
        position="sticky",
        background_color=rx.color("gray", 1),
        top="0px",
        z_index="5",
        border_bottom=styles.border,
    )
