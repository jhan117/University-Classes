import tkinter as tk
from tkinter import ttk

global prev_pos

works = []

root = tk.Tk()
root.title("Paint Board")
root.geometry("750x500")

root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=0)

for i in range(4):
    root.columnconfigure(i, weight=1)


def create_polygon(e, is_moving=True):
    global prev_pos
    (prev_x, prev_y) = prev_pos

    draw_canvas.delete("temp")

    color = color_var.get()
    color = "black" if color == " " else color

    if check_fill_var.get():
        fill_color = color_var.get()
    else:
        fill_color = ""

    if is_moving:
        if shape_var.get() == "직선":
            draw_canvas.create_line(prev_x, prev_y, e.x, e.y, fill=color, tags="temp")
        elif shape_var.get() == "사각형":
            draw_canvas.create_rectangle(prev_x, prev_y, e.x, e.y, outline=color, fill=fill_color, tags="temp")
        elif shape_var.get() == "타원":
            draw_canvas.create_oval(prev_x, prev_y, e.x, e.y, outline=color, fill=fill_color, tags="temp")
    else:
        if shape_var.get() == "직선":
            return draw_canvas.create_line(prev_x, prev_y, e.x, e.y, fill=color)
        elif shape_var.get() == "사각형":
            return draw_canvas.create_rectangle(prev_x, prev_y, e.x, e.y, outline=color, fill=fill_color)
        elif shape_var.get() == "타원":
            return draw_canvas.create_oval(prev_x, prev_y, e.x, e.y, outline=color, fill=fill_color)


def undo_btn():
    if works:
        draw_canvas.delete(works.pop())


def press_mouse(e):
    global prev_pos
    prev_pos = (e.x, e.y)


def motion_mouse(e):
    create_polygon(e)


def release_mouse(e):
    drew_shape = create_polygon(e, is_moving=False)

    if drew_shape:
        works.append(drew_shape)


# header
header = ttk.Frame(root)
header.grid(row=0, column=0, columnspan=1, sticky="nsew", padx=5, pady=(5, 0))

ttk.Button(header, text="모두 삭제",
           command=lambda: draw_canvas.delete(tk.ALL)).pack(side=tk.LEFT, fill="x", expand=True, padx=(0, 5))
ttk.Button(header, text="Undo",
           command=undo_btn).pack(side=tk.RIGHT, fill="x", expand=True)

# main
draw_canvas = tk.Canvas(root, bg="white")
draw_canvas.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# footer
footer = ttk.Frame(root)
footer.grid(row=2, column=0, columnspan=4, sticky="nsew", padx=5, pady=(0, 5))

shape_frame = ttk.LabelFrame(footer, text="모양 설정")
color_frame = ttk.LabelFrame(footer, text="색깔 설정")
fill_frame = ttk.LabelFrame(footer, text="색깔 채움 설정")

shape_frame.pack(side=tk.LEFT, fill="x", expand=True)
color_frame.pack(side=tk.LEFT, fill="x", expand=True, padx=5)
fill_frame.pack(side=tk.LEFT, fill="x", expand=True)

# footer_shape
shape_var = tk.StringVar(None, " ")
line = ttk.Radiobutton(shape_frame, text="직선", value="직선", variable=shape_var)
rect = ttk.Radiobutton(shape_frame, text="사각형", value="사각형", variable=shape_var)
oval = ttk.Radiobutton(shape_frame, text="타원", value="타원", variable=shape_var)

line.pack(side=tk.LEFT, fill="x", expand=True)
rect.pack(side=tk.LEFT, fill="x", expand=True)
oval.pack(side=tk.LEFT, fill="x", expand=True)

# footer_color
color_var = tk.StringVar(None, " ")
red = ttk.Radiobutton(color_frame, text="빨강", value="red", variable=color_var)
green = ttk.Radiobutton(color_frame, text="초록", value="green", variable=color_var)
blue = ttk.Radiobutton(color_frame, text="파랑", value="blue", variable=color_var)

red.pack(side=tk.LEFT, fill="x", expand=True)
green.pack(side=tk.LEFT, fill="x", expand=True)
blue.pack(side=tk.LEFT, fill="x", expand=True)

# footer_fill
check_fill_var = tk.BooleanVar()
check_fill = ttk.Checkbutton(fill_frame, text="색깔 채움 여부", variable=check_fill_var)

check_fill.pack()

# === event === #
draw_canvas.bind("<Button-1>", press_mouse)  # 클릭
draw_canvas.bind("<B1-Motion>", motion_mouse)  # 왼클릭하면서 움직임
draw_canvas.bind("<ButtonRelease-1>", release_mouse)  # 뗌

root.mainloop()
