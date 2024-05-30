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
        self.is_pen = True
        self.temp_lines = []

        # 위젯들 생성 및 배치
        self.header = ttk.Frame(self.root)
        self.draw_canvas = tk.Canvas(self.root, bg="white")
        self.footer = ttk.Notebook(self.root)
        self.tool_var = tk.IntVar(None, 1)  # 0: 지우개, 1: 펜
        self.size_var = tk.IntVar(None, 3)  # 1: 얇게, 3: 보통, 5: 굵게
        self.pen_color_var = tk.StringVar(None, "")
        self.shape_var = tk.StringVar(None, "line")
        self.color_var = tk.StringVar(None, "")
        self.check_fill_var = tk.BooleanVar()
        self.make_widgets()

        # === event === #
        self.draw_canvas.bind("<Button-1>", self.press_mouse)  # 클릭
        self.draw_canvas.bind("<B1-Motion>", self.motion_mouse)  # 왼클릭하면서 움직임
        self.draw_canvas.bind("<ButtonRelease-1>", self.release_mouse)  # 뗌
        self.footer.bind("<<NotebookTabChanged>>", self.change_cursor)  # tab 변경시

        self.root.mainloop()

    def press_mouse(self, e):
        self.prev_pos = (e.x, e.y)
        if self.is_pen:
            self.works.append(self.temp_lines)

    def motion_mouse(self, e):
        if self.is_pen:
            if self.tool_var.get():
                color = self.pen_color_var.get() if self.pen_color_var.get() else "black"
            else:
                color = "white"
            temp_line = self.draw_canvas.create_line(*self.prev_pos, e.x, e.y, fill=color, width=self.size_var.get())
            self.temp_lines.append(temp_line)
            self.prev_pos = (e.x, e.y)
        else:
            self.create_polygon(e)

    def release_mouse(self, e):
        if self.is_pen:
            self.temp_lines = []
        else:
            drew_shape = self.create_polygon(e, is_moving=False)
            if drew_shape:
                self.works.append(drew_shape)

    def change_cursor(self, e):
        if self.footer.index("current"):
            self.is_pen = False
            self.draw_canvas.config(cursor="tcross")
        else:
            self.is_pen = True
            self.draw_canvas.config(cursor="dotbox")

    def undo_work(self):
        if self.works:
            work = self.works.pop()
            if isinstance(work, list):
                for idx in work:
                    self.draw_canvas.delete(idx)
            else:
                self.draw_canvas.delete(work)

    def create_polygon(self, e, is_moving=True):
        # 변수 설정
        all_pos = (*self.prev_pos, e.x, e.y)
        cur_color = self.color_var.get()
        tag_name = "temp" if is_moving else ""
        color = cur_color if cur_color else "black"
        fill_color = cur_color if self.check_fill_var.get() else ""

        self.draw_canvas.delete("temp")

        if self.shape_var.get() == "line":
            return self.draw_canvas.create_line(*all_pos, fill=color, tags=tag_name)
        elif self.shape_var.get() == "rect":
            return self.draw_canvas.create_rectangle(*all_pos, outline=color, fill=fill_color, tags=tag_name)
        elif self.shape_var.get() == "oval":
            return self.draw_canvas.create_oval(*all_pos, outline=color, fill=fill_color, tags=tag_name)

    def make_widgets(self):
        args = {"side": tk.LEFT, "fill": tk.X, "expand": True}
        grid_args = {"column": 0, "sticky": tk.NSEW, "padx": 5}

        # == 생성 == #
        # in header
        all_delete_btn = ttk.Button(self.header, text="모두 삭제", command=lambda: self.draw_canvas.delete(tk.ALL))
        undo_btn = ttk.Button(self.header, text="Undo", command=self.undo_work)
        # in footer
        footer_pen = ttk.Frame(self.footer)
        footer_poly = ttk.Frame(self.footer)
        self.footer.add(footer_pen, text="그리기", padding=5)
        self.footer.add(footer_poly, text="도형", padding=5)

        # footer_pen
        tools_frame = ttk.LabelFrame(footer_pen, text="도구 설정")
        color_frame_pen = ttk.LabelFrame(footer_pen, text="색깔 설정")
        size_frame = ttk.LabelFrame(footer_pen, text="크기 설정")
        # footer_poly
        shape_frame = ttk.LabelFrame(footer_poly, text="모양 설정")
        color_frame = ttk.LabelFrame(footer_poly, text="색깔 설정")
        fill_frame = ttk.LabelFrame(footer_poly, text="색깔 채움 설정")
        # footer_pen_radiobutton
        ttk.Radiobutton(tools_frame, variable=self.tool_var, text="펜", value=1).pack(**args)
        ttk.Radiobutton(tools_frame, variable=self.tool_var, text="지우개", value=0).pack(**args)
        ttk.Radiobutton(size_frame, variable=self.size_var, text="얇게", value=1).pack(**args)
        ttk.Radiobutton(size_frame, variable=self.size_var, text="보통", value=3).pack(**args)
        ttk.Radiobutton(size_frame, variable=self.size_var, text="굵게", value=5).pack(**args)
        # footer_poly_radiobutton
        shape_list = {"line": "직선", "rect": "사각형", "oval": "타원"}
        color_list = {"red": "빨강", "green": "초록", "blue": "파랑"}
        var_list = {"shape": [shape_frame, self.shape_var, shape_list],
                    "color": [color_frame, self.color_var, color_list]}
        for key, values in var_list.items():
            for v, t in values[2].items():
                ttk.Radiobutton(values[0], variable=values[1], text=t, value=v).pack(**args)
                if key == "color":
                    ttk.Radiobutton(color_frame_pen, variable=self.pen_color_var, text=t, value=v).pack(**args)
        # footer_fill
        check_fill = ttk.Checkbutton(fill_frame, text="색깔 채움 여부", variable=self.check_fill_var)

        # == 배치 == #
        # 3프레임 (Header, Main, Footer)
        self.header.grid(row=0, columnspan=1, **grid_args, pady=(5, 0))
        self.draw_canvas.grid(row=1, columnspan=4, **grid_args, pady=5)
        self.footer.grid(row=2, columnspan=4, **grid_args, pady=(0, 5))
        # 하위 위젯들
        # in header
        all_delete_btn.pack(**args, padx=(0, 5))
        undo_btn.pack(**args)
        # in footer
        shape_frame.pack(**args)
        color_frame.pack(**args, padx=5)
        fill_frame.pack(**args)
        # footer_pen
        tools_frame.pack(**args)
        color_frame_pen.pack(**args, padx=5)
        size_frame.pack(**args)
        # footer_fill
        check_fill.pack()


if __name__ == "__main__":
    PaintBoard()
