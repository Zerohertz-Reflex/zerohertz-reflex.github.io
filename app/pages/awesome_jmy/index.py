import zerohertzLib as zz

import reflex as rx
from app.pages.awesome_jmy.util import dataloader_all, dataloader_ms, dataloader_phd
from app.styles.styles import awesome_am_colors
from app.templates.template import template


def dataloader2data(dataloader, tar):
    _data = dataloader.data[tar].value_counts().to_dict().items()
    hex_codes = [
        f"#{r:02X}{g:02X}{b:02X}"
        for r, g, b in zz.plot.color(len(_data), uint8=True, palette="coolwarm")
    ][::-1]
    data = [
        {"name": name, tar: value, "fill": color, "stroke": color}
        for (name, value), color in zip(_data, hex_codes)
    ]
    return data


def bar(dataloader, tar):
    data = dataloader2data(dataloader, tar)
    return rx.recharts.composed_chart(
        rx.recharts.bar(
            data_key=tar,
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(data_key="name", angle=45, tick_size=40),
        rx.recharts.y_axis(),
        rx.recharts.graphing_tooltip(),
        data=data,
        margin={
            "bottom": 60,
        },
        width="100%",
        height=350,
    )


def bar_top(dataloader, tar, top=30):
    data = []
    if tar == "복무인원":
        for _, name, _, a, b, _, c, d, _, _ in dataloader.ranked_data_org.iloc[
            :top
        ].values:
            data.append(
                {
                    "name": name,
                    "현역 복무인원": d - c,
                    "현역 편입인원": c,
                    "보충역 복무인원": b - a,
                    "보충역 편입인원": a,
                }
            )
    elif tar == "편입인원":
        for _, name, _, a, b, _, c, d, _, _ in dataloader.ranked_data_new.iloc[
            :top
        ].values:
            data.append({"name": name, "현역 편입인원": c, "보충역 편입인원": a})
    return rx.recharts.composed_chart(
        *[
            rx.recharts.bar(
                data_key=key,
                stroke=awesome_am_colors[key],
                fill=awesome_am_colors[key],
                stack_id="1",
            )
            for key in data[0].keys()
            if key != "name"
        ],
        rx.recharts.x_axis(type_="number"),
        rx.recharts.y_axis(data_key="name", type_="category", tick_size=10),
        rx.recharts.graphing_tooltip(),
        data=data,
        layout="vertical",
        margin={
            "left": 150,
        },
        width="100%",
        height=int(1900 / 30 * top),
    )


def pie(dataloader, tar):
    data = dataloader2data(dataloader, tar)
    return rx.recharts.pie_chart(
        rx.recharts.pie(
            data=data,
            data_key=tar,
            name_key="name",
            label=True,
        ),
        rx.recharts.graphing_tooltip(),
        width="100%",
        height=500,
    )


def visualization(dataloader):
    return rx.vstack(
        rx.heading(
            "연구분야",
            as_="h3",
            align="center",
            width="100%",
            size="4",
        ),
        bar(dataloader, "연구분야"),
        rx.heading(
            "위치",
            as_="h3",
            align="center",
            width="100%",
            size="4",
        ),
        pie(dataloader, "위치"),
        rx.heading(
            "복무인원 TOP 30",
            as_="h3",
            align="center",
            width="100%",
            size="4",
        ),
        bar_top(dataloader, "복무인원"),
        rx.heading(
            "편입인원 TOP 10",
            as_="h3",
            align="center",
            width="100%",
            size="4",
        ),
        bar_top(dataloader, "편입인원", 10),
        width="100%",
    )


@template(route="/awesome-jmy", title="Awesome JMY")
def awesome_jmy():
    return rx.vstack(
        rx.vstack(
            rx.heading(
                "🧑‍💻 전문연구요원을 위한 데이터 적재 및 시각화 🧑‍💻",
                as_="h1",
                align="center",
                width="100%",
            ),
            rx.link(
                rx.image(
                    src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg",
                ),
                href="https://github.com/sindresorhus/awesome",
                target="_blank",
            ),
            rx.link(
                rx.image(
                    src="https://img.shields.io/badge/awesome--jmy-800a0a?style=for-the-badge&logo=Awesome Lists&logoColor=white",
                ),
                href="https://github.com/Zerohertz/awesome-jmy",
                target="_blank",
            ),
            width="100%",
            align="center",
        ),
        rx.markdown(
            """
            - [**「병역법 제2조제16항」**](https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EB%B3%91%EC%97%AD%EB%B2%95/%EC%A0%9C2%EC%A1%B0) “전문연구요원”이란 학문과 기술의 연구를 위하여 제36조에 따라 전문연구요원(專門硏究要員)으로 편입되어 해당 전문 분야의 연구업무에 복무하는 사람을 말한다.
            </br>
            - [**「병역법 제3조제1항」**](https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EB%B3%91%EC%97%AD%EB%B2%95/%EC%A0%9C3%EC%A1%B0) 대한민국 국민인 남성은 헌법과 이 법에서 정하는 바에 따라 병역의무를 성실히 수행하여야 한다.
            """
        ),
        rx.vstack(
            rx.link(
                rx.heading(
                    "🎒 석사 전문연구요원 🎒",
                    as_="h2",
                    align="center",
                    width="100%",
                    size="5",
                ),
                href="awesome-jmy/ms",
            ),
            visualization(dataloader_ms),
            rx.link(
                rx.heading(
                    "🎓 박사 전문연구요원 🎓",
                    as_="h2",
                    align="center",
                    width="100%",
                    size="5",
                ),
                href="/awesome-jmy/phd",
            ),
            visualization(dataloader_phd),
            rx.link(
                rx.heading(
                    "💡 전체 전문연구요원 💡",
                    as_="h2",
                    align="center",
                    width="100%",
                    size="5",
                ),
                href="/awesome-jmy/all",
            ),
            visualization(dataloader_all),
            width="100%",
            align="center",
        ),
    )
