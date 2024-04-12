"""
[ 문제 ]
큰 사각형 안에 여러 개 작은 원
1. (0, 0) 중심점으로 한 변의 길이 400인 정사각형 그리기
2. 입력 받은 숫자만큼 정사각형 안에 원 그리기

[ 구현 ]
함수 목록:
- SetRainbowColor(i) : 무지개 색상 순서대로 i 번째에 색상 지정
- ReturnPos() : 무작위 숫자 생성 후 중심 위치와 삼각형 높이 반환
- DrawPolygon(x, y, r, multiple=True, half_height=None) : 중심 위치 x, y 기준으로 도형 하나 그리기
- DrawPolygons() : 도형 그리기 반복
- Draw() : 그리기 실행

Features:
- 선 색상 선택
- 채우기 색상 선택
- 반복할 도형 선택
- 무지개 색상 추가
- 중심 위치에서 그리기
"""

import math
import random
import inquirer
import turtle as t


class Drawing:
    def __init__(self, num, length, shape, line, color):
        """
        num : 도형 반복 횟수
        length : 테두리 한 변의 길이
        shape : 도형 모양
        line : 선 색상
        color : 채울 색상
        """
        self.N = num
        self.L = length
        self.HALF_L = self.L / 2
        self.SHAPE = shape
        self.RADIUS_MAX = 20  # 반지름 최대범위
        self.P_COLOR = line
        self.F_COLOR = color
        self.IS_RAINBOW_LINE = True if self.P_COLOR == "rainbow" else False
        self.IS_RAINBOW_COLOR = True if self.F_COLOR == "rainbow" else False

    def SetRainbowColor(self, i):
        """
        i : 도형 그린 횟수
        """
        if self.IS_RAINBOW_LINE:
            t.pencolor(RAINBOW_COLORS[i % 7])
        if self.IS_RAINBOW_COLOR:
            t.fillcolor(RAINBOW_COLORS[i % 7])

    def ReturnPos(self):
        half_height = None  # 삼각형 높이의 절반
        r = random.uniform(1, self.RADIUS_MAX)
        # x, y 범위 초깃값
        negative_x = -self.HALF_L + r
        positive_x = self.HALF_L - r
        negative_y = -self.HALF_L + r
        positive_y = self.HALF_L - r

        if self.SHAPE == "triangle":
            half_height = r * math.sqrt(3) / 2
            negative_y += half_height
            positive_y -= half_height

        x = random.uniform(negative_x, positive_x)
        y = random.uniform(negative_y, positive_y)

        return r, x, y, half_height

    def DrawPolygon(self, x, y, r, multiple=True, half_height=None):
        """
        x, y : 도형 중심 위치
        r : 반지름, 한 변의 길이의 절반
        multiple : 도형을 여러개 생성하는 경우인지
        half_height : 삼각형의 경우 높이의 절반
        """

        if (not multiple) or self.SHAPE == "square":  # 사각형
            t.teleport(x - r, y + r)
            for _ in range(4):
                t.forward(r * 2)
                t.right(90)
        elif self.SHAPE == "circle":
            t.teleport(x, y - r)
            t.circle(r)
        else:  # 삼각형
            t.teleport(x, y + half_height)
            for _ in range(3):
                t.forward(r * 2)
                t.right(120)

    def DrawPolygons(self):
        for i in range(self.N):
            [r, *center_pos, half_height] = self.ReturnPos()

            # 방향과 무지개 색상 설정
            t.seth(-60 if self.SHAPE == "triangle" else 0)
            self.SetRainbowColor(i)  # check for color

            if not self.IS_RAINBOW_LINE:
                t.pencolor(self.P_COLOR)
            if not self.IS_RAINBOW_COLOR and self.F_COLOR:
                t.fillcolor(self.F_COLOR)
            if self.F_COLOR:  # none이면 채우기 시작 안함
                t.begin_fill()

            self.DrawPolygon(*center_pos, r, half_height=half_height)
            t.end_fill()

    def Draw(self):
        self.DrawPolygon(0, 0, self.L / 2, multiple=False)  # 배경 박스 그리기
        self.DrawPolygons()  # 도형들 그리기 시작


if __name__ == "__main__":
    # Constants
    L = 400  # 한 변의 길이
    RAINBOW_COLORS = [
        "#e81416",
        "#ffa500",
        "#faeb36",
        "#79c314",
        "#487de7",
        "#4b369d",
        "#70369d",
    ]  # 무지개 색상 코드
    SHAPE_LIST = ["circle", "triangle", "square"]
    LINE_COLOR_LIST = ["black", "red", "blue", "green", "rainbow"]
    FILL_COLOR_LIST = ["none", "yellow", "margenta", "cyan", "black", "rainbow"]

    # cmd
    shape_a = inquirer.prompt(
        [
            inquirer.List(
                "shape",
                message="그릴 모양을 선택해주세요",
                choices=SHAPE_LIST,
            ),
        ]
    )["shape"]
    line_a = inquirer.prompt(
        [
            inquirer.List(
                "line",
                message="선 색상을 선택해주세요",
                choices=LINE_COLOR_LIST,
            ),
        ]
    )["line"]
    color_a = inquirer.prompt(
        [
            inquirer.List(
                "color",
                message="채울 색상을 선택해주세요",
                choices=FILL_COLOR_LIST,
            ),
        ]
    )["color"]
    # margenta 인식 안돼서 색상 코드로 변환
    color_a = (
        False if color_a == "none" else "#ff00ff" if color_a == "margenta" else color_a
    )

    # turtle 시작
    t.speed(0)
    t.bgcolor("#cccccc")  # 밝은 색 보이게
    t.hideturtle()  # 커서 숨기기
    circle_count = t.numinput("도형 그리기", "도형의 개수 : ")
    circle_count = (
        0 if circle_count is None else int(circle_count)
    )  # 미입력시 0으로 설정

    # 그리기 시작
    Drawing(circle_count, L, shape_a, line_a, color_a).Draw()

    # 화면 클릭시 종료
    t.exitonclick()
