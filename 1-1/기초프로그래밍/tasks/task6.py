import tkinter as tk
from tkinter import ttk


class PaintBoard:
    def __init__(self):
        # 화면 초기 설정
        self.root = tk.Tk()
        self.root.title("Paint Board")
        self.root.geometry("750x500")
        self.root.rowconfigure(0, weight=0)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=0)
        for i in range(4):
            self.root.columnconfigure(i, weight=1)

        # 초기 변수
        self.works = []
        self.prev_pos = (0, 0)

        # 위젯들 생성 및 배치
        self.header = ttk.Frame(self.root)
        self.draw_canvas = tk.Canvas(self.root, bg="white")
        self.footer = ttk.Frame(self.root)
        self.shape_var = tk.StringVar(None, "")
        self.color_var = tk.StringVar(None, "")
        self.check_fill_var = tk.BooleanVar()
        self.make_widgets()

        # === event === #
        self.draw_canvas.bind("<Button-1>", self.press_mouse)  # 클릭
        self.draw_canvas.bind("<B1-Motion>", self.motion_mouse)  # 왼클릭하면서 움직임
        self.draw_canvas.bind("<ButtonRelease-1>", self.release_mouse)  # 뗌

        self.root.mainloop()

    def press_mouse(self, e):
        self.prev_pos = (e.x, e.y)

    def motion_mouse(self, e):
        self.create_polygon(e)

    def release_mouse(self, e):
        drew_shape = self.create_polygon(e, is_moving=False)
        if drew_shape:
            self.works.append(drew_shape)

    def create_polygon(self, e, is_moving=True):
        # 변수 설정
        all_pos = (*self.prev_pos, e.x, e.y)
        cur_color = self.color_var.get()
        tag_name = "temp" if is_moving else ""
        color = cur_color if cur_color else "black"
        fill_color = cur_color if self.check_fill_var.get() else ""

        self.draw_canvas.delete("temp")

        if self.shape_var.get() == "직선":
            return self.draw_canvas.create_line(*all_pos, fill=color, tags=tag_name)
        elif self.shape_var.get() == "사각형":
            return self.draw_canvas.create_rectangle(*all_pos, outline=color, fill=fill_color, tags=tag_name)
        elif self.shape_var.get() == "타원":
            return self.draw_canvas.create_oval(*all_pos, outline=color, fill=fill_color, tags=tag_name)

    def make_widgets(self):
        # == 생성 == #
        # in header
        all_delete_btn = ttk.Button(self.header, text="모두 삭제", command=lambda: self.draw_canvas.delete(tk.ALL))
        undo_btn = ttk.Button(self.header, text="Undo",
                              command=lambda: self.draw_canvas.delete(self.works.pop()) if self.works else None)
        # in footer
        shape_frame = ttk.LabelFrame(self.footer, text="모양 설정")
        color_frame = ttk.LabelFrame(self.footer, text="색깔 설정")
        fill_frame = ttk.LabelFrame(self.footer, text="색깔 채움 설정")
        # footer_shape
        line = ttk.Radiobutton(shape_frame, text="직선", value="직선", variable=self.shape_var)
        rect = ttk.Radiobutton(shape_frame, text="사각형", value="사각형", variable=self.shape_var)
        oval = ttk.Radiobutton(shape_frame, text="타원", value="타원", variable=self.shape_var)
        # footer_color
        red = ttk.Radiobutton(color_frame, text="빨강", value="red", variable=self.color_var)
        green = ttk.Radiobutton(color_frame, text="초록", value="green", variable=self.color_var)
        blue = ttk.Radiobutton(color_frame, text="파랑", value="blue", variable=self.color_var)
        # footer_fill
        check_fill = ttk.Checkbutton(fill_frame, text="색깔 채움 여부", variable=self.check_fill_var)

        # == 배치 == #
        # 3프레임 (Header, Main, Footer)
        grid_args = {"column": 0, "sticky": tk.NSEW, "padx": 5}
        self.header.grid(row=0, columnspan=1, **grid_args, pady=(5, 0))
        self.draw_canvas.grid(row=1, columnspan=4, **grid_args, pady=5)
        self.footer.grid(row=2, columnspan=4, **grid_args, pady=(0, 5))
        # 하위 위젯들
        args = {"side": tk.LEFT, "fill": tk.X, "expand": True}
        # in header
        all_delete_btn.pack(**args, padx=(0, 5))
        undo_btn.pack(side=tk.RIGHT, fill="x", expand=True)
        # in footer
        shape_frame.pack(**args)
        color_frame.pack(**args, padx=5)
        fill_frame.pack(**args)
        # footer_shape
        line.pack(**args)
        rect.pack(**args)
        oval.pack(**args)
        # footer_color
        red.pack(**args)
        green.pack(**args)
        blue.pack(**args)
        # footer_fill
        check_fill.pack()


if __name__ == "__main__":
    PaintBoard()
