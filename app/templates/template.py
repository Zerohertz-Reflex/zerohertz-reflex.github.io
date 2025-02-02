from typing import Callable

import reflex as rx
from app.components.navbar import navbar
from app.components.sidebar import sidebar
from app.styles import styles
from app.styles.theme import theme_config

default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]


def template(
    *,
    route: str | None = None,
    title: str | None = None,
    description: str | None = None,
    meta: str | None = None,
    script_tags: list[rx.Component] | None = None,
    on_load: rx.EventHandler | list[rx.EventHandler] | None = None,
) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        all_meta = [*default_meta, *(meta or [])]

        def templated_page():
            return rx.flex(
                navbar(),
                sidebar(),
                rx.flex(
                    rx.vstack(
                        page_content(),
                        width="100%",
                        **styles.template_content_style,
                        align="center",
                    ),
                    width="100%",
                    **styles.template_page_style,
                    max_width=[
                        "100%",
                        "100%",
                        "100%",
                        "100%",
                        "100%",
                        styles.max_width,
                    ],
                ),
                flex_direction=[
                    "column",
                    "column",
                    "column",
                    "column",
                    "column",
                    "row",
                ],
                width="100%",
                margin="auto",
                position="relative",
            )

        @rx.page(
            route=route,
            title=title,
            description=description,
            meta=all_meta,
            script_tags=script_tags,
            on_load=on_load,
        )
        def theme_wrap():
            return rx.theme(
                templated_page(),
                has_background=True,
                **theme_config.model_dump(),
            )

        return theme_wrap

    return decorator
