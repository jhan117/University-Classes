import turtle as t
import os
from PIL import Image
import numpy as np
import requests

# 도트 그림 코드
class Paint():
    def __init__(self):
        t.colormode(255)
        t.shape("square")
        t.shapesize(0.5) # 10 pixel

        self.PIXEL = 16
        self.BEGIN_X = -(self.PIXEL / 2 * 10)
        self.BEGIN_Y = self.PIXEL / 2 * 10
        self.URL = "https://avatars.githubusercontent.com/u/78463832?v=4"

        self.image = Image.open(requests.get(self.URL, stream=True).raw)
        self.image.thumbnail((self.PIXEL, self.PIXEL))
        self.pixel_list = np.array(self.image)

    # 작업 코드
    def work(self):
        t.teleport(self.BEGIN_X, self.BEGIN_Y)
        for y, colors in enumerate(self.pixel_list):
            for x, color in enumerate(colors):
                t.color(color)
                t.stamp()
                t.teleport(self.BEGIN_X + (x + 1) * 10)
            t.teleport(self.BEGIN_X, self.BEGIN_Y + (y + 1) * (-10))

# 과제 코드
EXPRESS = " "
COLOR = "white"
D = 90

# 가로 세로 입력
while True:
    pos = input("직사각형의 가로와 세로를 입력하세요 : ")

    # 쉼표 입력시에도 허용
    if "," in pos:
        EXPRESS = ","
    input_list = pos.split(EXPRESS)

    # 입력 예외
    if len(input_list) != 2:
        os.system("cls")
        print("다시 입력해주세요...")
        continue

    x, y = map(int, input_list)
    os.system("cls")
    break

# 색상 선택 입력
while True:
    in_color = input("1) 빨간색 2) 초록색 3) 파란색 4) 직접 입력\n채울 색깔의 번호를 선택해주세요 : ")

    if in_color == "1":
        COLOR = "red"
        break
    elif in_color == "2":
        COLOR = "green"
        break
    elif in_color == "3":
        COLOR = "blue"
        break
    elif in_color == "4":
        # 너무 길어지니 예외 코드 작성 안함
        COLOR = input("직접 입력해주세요 : ")
        if '"' in COLOR:
            COLOR = COLOR.strip('"')
        break
    else:
        os.system("cls")
        print("다시 입력해주세요...")
        continue

# 추가적으로 필요한 변수들 저장
half_x = x / 2
half_y = y / 2
area = x * y # 넓이
perimeter = 2 * (x + y) # 둘레의 길이

# 정보 출력
print(f"입력하신 정보는 가로 : {x}, 세로 : {y}, 색상 : {COLOR} 입니다.")
print(f"직사각형의 면적은 {area}이며, 둘레는 {perimeter}입니다.")

# turtle 코드
t.fillcolor(COLOR)

# 사각형 그리기
t.begin_fill()
t.teleport(-half_x, half_y)
for _ in range(2):
    t.forward(x)
    t.right(D)
    t.forward(y)
    t.right(D)
t.end_fill()

# 중앙 십자가
t.teleport(-half_x, 0)
t.forward(x)
t.teleport(0, -half_y)
t.setheading(D)
t.forward(y)

# 보너스 그림 및 종료 입력
while True:
    quit_input = input("\n보너스로 강아지 그림을 볼 수 있는데... 종료하시겠습니까?\n1) 네 2) 그림 보기\n")
    if quit_input == "1":
        # 프로그램 종료
        t.bye()
        quit()
    elif quit_input == "2":
        # 보너스 그림
        os.system('cls')
        print("저희 집 강아지입니다 ㅎ... 시간 관계상 16칸으로 각 pixel의 크기는 10으로 지정했습니다")
        t.clearscreen()
        Paint().work()
        continue
    else:
        os.system("cls")
        print("다시 입력해주세요...")
        continue