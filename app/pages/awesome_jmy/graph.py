import os

import pandas as pd

import reflex as rx
from app.pages.awesome_jmy.util import _name
from app.styles.styles import awesome_am_colors
from app.templates.template import template


def graph(path, name):
    data = pd.read_csv(
        os.path.join(path, _name(name) + ".tsv"),
        sep="\t",
        header=None,
        names=[
            "날짜",
            "업체명",
            "보충역 편입인원",
            "보충역 복무인원",
            "현역 편입인원",
            "현역 복무인원",
            "편입인원",
            "복무인원",
        ],
        dtype={"날짜": str},
    )
    data["날짜"] = pd.to_datetime(data["날짜"], format="%Y%m%d").dt.strftime("%Y-%m-%d")
    ylim = int(data["복무인원"].max() * 1.15)
    data = data.to_dict(orient="records")
    return rx.vstack(
        rx.heading(data[0]["업체명"], as_="h1", align="center", width="100%"),
        rx.recharts.composed_chart(
            rx.recharts.area(
                data_key="현역 복무인원",
                stroke=awesome_am_colors["현역 복무인원"],
                fill=awesome_am_colors["현역 복무인원"],
                stack_id="1",
            ),
            rx.recharts.area(
                data_key="보충역 복무인원",
                stroke=awesome_am_colors["보충역 복무인원"],
                fill=awesome_am_colors["보충역 복무인원"],
                stack_id="1",
            ),
            rx.recharts.line(
                data_key="복무인원",
                stroke=awesome_am_colors["복무인원"],
                dot={
                    "stroke": awesome_am_colors["복무인원"],
                    "fill": awesome_am_colors["복무인원"],
                },
            ),
            rx.recharts.x_axis(data_key="날짜"),
            rx.recharts.y_axis(type_="number", domain=[0, ylim]),
            rx.recharts.graphing_tooltip(),
            rx.recharts.legend(vertical_align="top"),
            data=data,
            sync_id="1",
            height=350,
            width="100%",
        ),
        rx.recharts.composed_chart(
            rx.recharts.area(
                data_key="현역 편입인원",
                stroke=awesome_am_colors["현역 편입인원"],
                fill=awesome_am_colors["현역 편입인원"],
                stack_id="1",
            ),
            rx.recharts.area(
                data_key="보충역 편입인원",
                stroke=awesome_am_colors["보충역 편입인원"],
                fill=awesome_am_colors["보충역 편입인원"],
                stack_id="1",
            ),
            rx.recharts.line(
                data_key="편입인원",
                stroke=awesome_am_colors["편입인원"],
                dot={
                    "stroke": awesome_am_colors["편입인원"],
                    "fill": awesome_am_colors["편입인원"],
                },
            ),
            rx.recharts.x_axis(data_key="날짜"),
            rx.recharts.y_axis(type_="number", domain=[0, ylim]),
            rx.recharts.graphing_tooltip(),
            rx.recharts.legend(vertical_align="top"),
            data=data,
            sync_id="1",
            height=350,
            width="100%",
        ),
        width="100%",
    )
