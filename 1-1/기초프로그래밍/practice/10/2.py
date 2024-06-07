"""
[실습: 이미지 처리 결과 출력하기]

실행 예시와 같이 윈도우의 왼쪽에는 항상 원본 파일("lenna.png")의 이미지를 출력하고 오른쪽에는 아래쪽 버튼에 해당하는 이미지 처리 결과를 출력하라.
이미지 처리버튼은 4가지로 좌우 대칭, 상하 대칭, FIND_EDGES, EMBOSS가 있다.
- 최초 실행 시에는 왼쪽과 오른쪽 모두 원본 파일을 출력한다.
"""
import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
from tkinter import ttk


def resize_window(e):
    global origin_img_id, convert_img_id, tk_convert_img

    origin_img_width = 512 if origin_img.winfo_width() < 512 else origin_img.winfo_width()
    origin_img_height = 512 if origin_img.winfo_height() < 512 else origin_img.winfo_height()
    convert_img_width = 512 if convert_img.winfo_width() < 512 else convert_img.winfo_width()
    convert_img_height = 512 if convert_img.winfo_height() < 512 else convert_img.winfo_height()

    origin_img.delete(origin_img_id)
    origin_img_id = origin_img.create_image(origin_img_width / 2, origin_img_height / 2,
                                            image=tk_origin_image)
    convert_img.delete(convert_img_id)
    convert_img_id = convert_img.create_image(convert_img_width / 2, convert_img_height / 2,
                                              image=tk_convert_img)


def convert_image(btn):
    global convert_img_id, tk_convert_img

    convert_img.delete(convert_img_id)
    tk_convert_img = ImageTk.PhotoImage(convert_img_list[btn])
    convert_img_id = convert_img.create_image(convert_img.winfo_width() / 2, convert_img.winfo_height() / 2,
                                              image=tk_convert_img)


# == 초기 설정 == #
root = tk.Tk()
origin_image = Image.open("resources/lenna.png")
img_width, img_height = origin_image.size
convert_img_list = {"좌우 대칭": origin_image.transpose(Image.Transpose.FLIP_LEFT_RIGHT),
                    "상하 대칭": origin_image.transpose(Image.Transpose.FLIP_TOP_BOTTOM),
                    "Find Edges": origin_image.filter(ImageFilter.FIND_EDGES),
                    "Emboss": origin_image.filter(ImageFilter.EMBOSS)}
tk_origin_image = ImageTk.PhotoImage(origin_image)
tk_convert_img = ImageTk.PhotoImage(origin_image)

# == 배치 == #
# root
img_frame = tk.Frame(root)
buttons_frame = tk.Frame(root)
img_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
buttons_frame.pack(side=tk.BOTTOM, fill=tk.X)
# img_frame
origin_img = tk.Canvas(img_frame, width=img_width, height=img_height)
convert_img = tk.Canvas(img_frame, width=img_width, height=img_height)
origin_img.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
convert_img.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
# buttons_frame
flip_EW_btn = ttk.Button(buttons_frame, text="좌우 대칭", command=lambda: convert_image("좌우 대칭"))
flip_NS_btn = ttk.Button(buttons_frame, text="상하 대칭", command=lambda: convert_image("상하 대칭"))
find_edges_btn = ttk.Button(buttons_frame, text="Find Edges", command=lambda: convert_image("Find Edges"))
emboss_btn = ttk.Button(buttons_frame, text="Emboss", command=lambda: convert_image("Emboss"))
flip_EW_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
flip_NS_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
find_edges_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
emboss_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)

# == 이미지 == #
origin_img_id = origin_img.create_image(img_width/2, img_height/2, image=tk_origin_image)
convert_img_id = convert_img.create_image(img_width/2, img_height/2, image=tk_convert_img)

# == 이벤트 == #
origin_img.bind("<Configure>", resize_window)
root.mainloop()
