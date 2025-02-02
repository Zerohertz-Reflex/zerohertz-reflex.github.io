import warnings
from glob import glob

import pandas as pd

warnings.filterwarnings("ignore")


def _name(name):
    return (
        name.replace("(", "").replace(")", "").replace("/", "").replace(" ", "").lower()
    )


class DataLoader:
    def __init__(self, file_name, degree):
        self.time = file_name[-12:-4]
        self.data = pd.read_excel(file_name)
        """
        NOTE: "벤처기업부설연구소", "중견기업부설연구소", "중소기업부설연구소"를 제외한 모든 업종은 박사 전문연구요원으로 간주
        과기원
        과기원부설연구소
        국가기관 등 연구소
        기초연구연구기관
        대기업부설연구소
        대학원연구기관
        방산연구기관
        벤처기업부설연구소
        자연계대학부설연구기관
        정부출연연구소
        중견기업부설연구소
        중소기업부설연구소
        지역혁신센터연구소
        특정연구소
        """
        if degree == 1:
            self.data = self.data[
                (self.data["업종"] == "벤처기업부설연구소")
                | (self.data["업종"] == "중견기업부설연구소")
                | (self.data["업종"] == "중소기업부설연구소")
            ]
        elif degree == 2:
            self.data = self.data[
                ~(
                    (self.data["업종"] == "벤처기업부설연구소")
                    | (self.data["업종"] == "중견기업부설연구소")
                    | (self.data["업종"] == "중소기업부설연구소")
                )
            ]
        self.data["위치"] = (
            self.data["주소"]
            .str.replace("서울특별시 ", "서울특별시")
            .str.replace("경기도 ", "경기도")
            .str.split(" ")
            .str[0]
            .str.replace("서울특별시", "서울특별시 ")
            .str.replace("경기도", "경기도 ")
        )
        self.data["편입인원"] = (
            self.data["보충역 편입인원"] + self.data["현역 편입인원"]
        )
        self.data["복무인원"] = (
            self.data["보충역 복무인원"] + self.data["현역 복무인원"]
        )
        self.ranked_data_org = self.data.sort_values(
            by=["복무인원", "업체명"], ascending=[False, True]
        ).loc[
            :,
            [
                "순번",
                "업체명",
                "보충역 배정인원",
                "보충역 편입인원",
                "보충역 복무인원",
                "현역 배정인원",
                "현역 편입인원",
                "현역 복무인원",
                "편입인원",
                "복무인원",
            ],
        ]
        self.ranked_data_new = self.data.sort_values(
            by=["편입인원", "업체명"], ascending=[False, True]
        ).loc[
            :,
            [
                "순번",
                "업체명",
                "보충역 배정인원",
                "보충역 편입인원",
                "보충역 복무인원",
                "현역 배정인원",
                "현역 편입인원",
                "현역 복무인원",
                "편입인원",
                "복무인원",
            ],
        ]


graph = """
@template(route="/awesome-jmy/{idx}", title="{name}")
def awesome_jmy_{idx}():
    path = "awesome-jmy/prop/time/data/"
    name = "{name}"
    return graph(path, name)
"""

paths = glob("awesome-jmy/data/*.xls")
paths.sort()
file_name = paths[-1]

dataloader_all = DataLoader(file_name, 0)
dataloader_ms = DataLoader(file_name, 1)
dataloader_phd = DataLoader(file_name, 2)


if __name__ == "__main__":
    with open("app/pages/awesome_jmy/graph.py", "a") as file:
        for (
            idx,
            name,
            a1,
            a2,
            a3,
            b1,
            b2,
            b3,
            t1,
            t2,
        ) in dataloader_all.ranked_data_org.values[:3]:
            print(idx)
            print(graph.format(idx=idx, name=name))
            file.write(graph.format(idx=idx, name=name))
