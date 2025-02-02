import reflex as rx
from app.pages.awesome_jmy.util import dataloader_all, dataloader_ms, dataloader_phd
from app.templates.template import template


def table(dataloader):
    return rx.vstack(
        rx.heading(
            "🧑‍💻 전문연구요원 복무인원 순위 🧑‍💻",
            as_="h1",
            align="center",
            width="100%",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("업체명"),
                    rx.table.column_header_cell("보충역 배정인원"),
                    rx.table.column_header_cell("보충역 편입인원"),
                    rx.table.column_header_cell("보충역 복무인원"),
                    rx.table.column_header_cell("현역 배정인원"),
                    rx.table.column_header_cell("현역 편입인원"),
                    rx.table.column_header_cell("현역 복무인원"),
                    rx.table.column_header_cell("총 편입인원"),
                    rx.table.column_header_cell("총 복무인원"),
                ),
            ),
            rx.table.body(
                *[
                    rx.table.row(
                        rx.table.row_header_cell(
                            rx.link(name, href=f"/awesome-jmy/{idx}")
                        ),
                        rx.table.cell(a1),
                        rx.table.cell(a2),
                        rx.table.cell(a3),
                        rx.table.cell(b1),
                        rx.table.cell(b2),
                        rx.table.cell(b3),
                        rx.table.cell(t1),
                        rx.table.cell(t2),
                    )
                    for idx, name, a1, a2, a3, b1, b2, b3, t1, t2 in dataloader.ranked_data_org.values
                ]
            ),
            width="100%",
        ),
    )


@template(route="/awesome-jmy/all", title="전체 전문연구요원")
def table_all():
    return table(dataloader_all)


@template(route="/awesome-jmy/ms", title="석사 전문연구요원")
def table_ms():
    return table(dataloader_ms)


@template(route="/awesome-jmy/phd", title="박사 전문연구요원")
def table_phd():
    return table(dataloader_phd)
