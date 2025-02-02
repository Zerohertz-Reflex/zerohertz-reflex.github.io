import reflex as rx
from app.styles import styles


def sidebar_header() -> rx.Component:
    return rx.hstack(
        # rx.color_mode_cond(
        #     rx.image(src="/reflex_black.svg", height="1.5em"),
        #     rx.image(src="/reflex_white.svg", height="1.5em"),
        # ),
        rx.spacer(),
        align="center",
        width="100%",
        padding="0.35em",
        margin_bottom="1em",
    )


def sidebar_footer() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.icon("github", size=18),
            href="https://github.com/Zerohertz/reflex",
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
        rx.spacer(),
        rx.color_mode.button(style={"opacity": "0.8", "scale": "0.95"}),
        justify="start",
        align="center",
        width="100%",
        padding="0.35em",
    )


def sidebar_item_icon(icon: str) -> rx.Component:
    return rx.icon(icon, size=18)


def sidebar_item(text: str, url: str) -> rx.Component:
    # active = (rx.State.router.page.path == url.lower()) | (
    #     (rx.State.router.page.path == "/") & text == "Overview"
    # )

    return rx.link(
        rx.hstack(
            rx.match(
                text,
                ("Overview", sidebar_item_icon("home")),
                ("Table", sidebar_item_icon("table-2")),
                ("About", sidebar_item_icon("book-open")),
                ("Profile", sidebar_item_icon("user")),
                ("Settings", sidebar_item_icon("settings")),
                sidebar_item_icon("layout-dashboard"),
            ),
            rx.text(text, size="3", weight="regular"),
            # color=rx.cond(
            #     active,
            #     styles.accent_text_color,
            #     styles.text_color,
            # ),
            # style={
            #     "_hover": {
            #         "background_color": rx.cond(
            #             active,
            #             styles.accent_bg_color,
            #             styles.gray_bg_color,
            #         ),
            #         "color": rx.cond(
            #             active,
            #             styles.accent_text_color,
            #             styles.text_color,
            #         ),
            #         "opacity": "1",
            #     },
            #     "opacity": rx.cond(
            #         active,
            #         "1",
            #         "0.95",
            #     ),
            # },
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


def sidebar() -> rx.Component:
    from reflex.page import get_decorated_pages

    ordered_page_routes = [
        "/",
        "/table",
        "/about",
        "/profile",
        "/settings",
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
    return rx.flex(
        rx.vstack(
            sidebar_header(),
            rx.vstack(
                *[
                    sidebar_item(
                        text=page.get("title", page["route"].strip("/").capitalize()),
                        url=page["route"],
                    )
                    for page in ordered_pages
                    if page["route"].count("/") < 3
                ],
                spacing="1",
                width="100%",
            ),
            rx.spacer(),
            sidebar_footer(),
            justify="end",
            align="end",
            width=styles.sidebar_content_width,
            height="100dvh",
            padding="1em",
        ),
        display=["none", "none", "none", "none", "none", "flex"],
        max_width=styles.sidebar_width,
        width="auto",
        height="100%",
        position="sticky",
        justify="end",
        top="0px",
        left="0px",
        flex="1",
        bg=rx.color("gray", 2),
    )
