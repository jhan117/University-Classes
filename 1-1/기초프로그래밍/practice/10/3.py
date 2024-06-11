"""
실습: 마우스 클릭 위치에 원 그리기

"lenna.png" 이미지를 tkinter 캔버스에 출력한 후 이미지의 임의의 위치에서 왼쪽 마우스 버튼을 클릭할 때마다 해당 위치를 중심점으로 하는 작은 원을 그려 보라.
원의 색상은 흰색으로 설정한다. 이 원은 이미지 자체에 반영되어야 한다.
왼쪽 마우스 버튼 클릭 시 실행되는 이벤트 처리 함수는 다음과 같은 절차로 진행된다.

- 캔버스 위젯에 출력되어 있는 이미지를 삭제한다.
- ImageDraw 객체의 ellipse 메소드를 통해 이미지의 해당 위치에 원을 그린다.
- ImageTk의 PhotoImage 메소드를 통해 tkinter 이미지를 반환받은 후 캔버스 위젯에 출력한다.
"""
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw


def draw_ellipse(e):
    global tk_image

    draw = ImageDraw.Draw(image)
    draw.ellipse((e.x - 5, e.y - 5, e.x + 5, e.y + 5), outline=(255, 255, 255))
    tk_image = ImageTk.PhotoImage(image)

    canvas.delete(tk.ALL)
    canvas.create_image(img_width/2, img_height/2, image=tk_image)


root = tk.Tk()
image = Image.open("resources/lenna.png")
img_width, img_height = image.size
tk_image = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=img_width, height=img_height)
canvas.pack(fill=tk.BOTH, expand=True)
canvas.create_image(img_width/2, img_height/2, image=tk_image, tags="img")

root.bind("<Button-1>", draw_ellipse)

root.mainloop()
