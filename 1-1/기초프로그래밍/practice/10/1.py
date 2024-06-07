"""
[실습: 이미지 파일 출력하기]

"lenna.png" 파일의 이미지를 tkinter 윈도우로 출력하되 항상 윈도우의 오른쪽 아래에 위치하도록 만들어보라.
"""
import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()

origin_image = Image.open("resources/lenna.png")
img_width, img_height = origin_image.size
tk_image = ImageTk.PhotoImage(origin_image)

canvas = tk.Canvas(root, width=img_width, height=img_height)
canvas.pack(expand=True, fill=tk.BOTH)

img_id = canvas.create_image(0, 0, image=tk_image)

print(canvas.winfo_reqwidth(), img_width)


def resize_window(e):
    global img_id

    canvas.delete(img_id)
    img_id = canvas.create_image(e.width - img_width/2, e.height - img_height/2,
                                 image=tk_image)


canvas.bind("<Configure>", resize_window)
root.mainloop()
