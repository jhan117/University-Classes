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

        # == variables of widget == #
        self.tool_var = tk.IntVar(None, 1)  # 0: 지우개, 1: 펜
        self.size_var = tk.IntVar(None, 3)  # 1: 얇게, 3: 보통, 5: 굵게
        self.pen_color_var = tk.StringVar(None, "")
        self.shape_var = tk.StringVar(None, "line")
        self.color_var = tk.StringVar(None, "")
        self.check_fill_var = tk.BooleanVar()

        # == widgets == #
        self.header = ttk.Frame(self.root)
        self.draw_canvas = tk.Canvas(self.root, bg="white")
        self.footer = ttk.Notebook(self.root)
        self.make_widgets()

        # === event === #
        self.draw_canvas.bind("<Button-1>", self.press_mouse)  # 클릭
        self.draw_canvas.bind("<B1-Motion>", self.motion_mouse)  # 왼클릭하면서 움직임
        self.draw_canvas.bind("<ButtonRelease-1>", self.release_mouse)  # 뗌
        self.footer.bind("<<NotebookTabChanged>>", self.change_cursor)  # tab 변경시

        self.root.mainloop()

    def press_mouse(self, e):
        """<Button-1>"""
        self.prev_pos = (e.x, e.y)
        self.works.append(self.temp_lines) if self.is_pen else None

    def motion_mouse(self, e):
        """<B1-Motion>"""
        if self.is_pen:
            if self.tool_var.get():     # 연필
                color = self.pen_color_var.get() if self.pen_color_var.get() else "black"
            else:   # 지우개
                color = "white"
            temp_line = self.draw_canvas.create_line(*self.prev_pos, e.x, e.y, fill=color, width=self.size_var.get())
            self.temp_lines.append(temp_line)
            self.prev_pos = (e.x, e.y)
        else:
            self.create_polygon(e)

    def release_mouse(self, e):
        """<ButtonRelease-1>"""
        if self.is_pen:
            self.temp_lines = []
        else:
            drew_shape = self.create_polygon(e, is_moving=False)
            if drew_shape:
                self.works.append(drew_shape)

    def change_cursor(self, e):
        cursor = ""
        if self.footer.index("current"):
            self.is_pen = False
            cursor = "tcross"
        else:
            self.is_pen = True
            cursor = "dotbox"
        self.draw_canvas.config(cursor=cursor)

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

        # == 생성 및 배치 == #
        self.header.grid(row=0, columnspan=1, **grid_args, pady=(5, 0))
        self.draw_canvas.grid(row=1, columnspan=4, **grid_args, pady=5)
        self.footer.grid(row=2, columnspan=4, **grid_args, pady=(0, 5))
        # header: 모두 삭제 및 Undo 버튼
        ttk.Button(self.header, text="모두 삭제", command=lambda: self.draw_canvas.delete(tk.ALL)).pack(**args, padx=(0, 5))
        ttk.Button(self.header, text="Undo", command=self.undo_work).pack(side=tk.RIGHT, fill="x", expand=True)
        # footer
        footer_pen = ttk.Frame(self.footer)
        footer_poly = ttk.Frame(self.footer)
        self.footer.add(footer_pen, text="그리기", padding=5)
        self.footer.add(footer_poly, text="도형", padding=5)
        # footer widgets
        make_labelframe_dict = {}       # {"pen": {"도구 설정": frame...
        # [frame, text]
        labelframe_dict = {"pen": [footer_pen, ["도구 설정", "색깔 설정", "크기 설정"]],
                           "poly": [footer_poly, ["모양 설정", "색깔 설정", "색깔 채움 설정"]]}
        # [variable, text, value]
        detail_dict = {"pen": {"도구 설정": [self.tool_var, ["펜", "지우개"], [1, 0]],
                               "색깔 설정": [self.pen_color_var, ["빨강", "초록", "파랑"], ["red", "green", "blue"]],
                               "크기 설정": [self.size_var, ["얇게", "보통", "굵게"], [1, 3, 5]]},
                       "poly": {"모양 설정": [self.shape_var, ["직선", "사각형", "타원"], ["line", "rect", "oval"]],
                                "색깔 설정": [self.color_var, ["빨강", "초록", "파랑"], ["red", "green", "blue"]],
                                "색깔 채움 설정": [self.check_fill_var, "색깔 채움 여부", None]}}
        for k, v_list in labelframe_dict.items():
            master = v_list[0]
            temp_dict = {}
            for t in v_list[1]:
                temp_frame = ttk.LabelFrame(master, text=t)
                temp_dict[t] = temp_frame
                if t == "색깔 채움 설정":
                    temp_frame.pack()
                elif t == "색깔 설정":
                    temp_frame.pack(**args, padx=5)
                else:
                    temp_frame.pack(**args)
            make_labelframe_dict[k] = temp_dict
        for k, name in make_labelframe_dict.items():
            for key, frame in name.items():
                [var, text, value] = detail_dict[k][key]
                if key == "색깔 채움 설정":
                    ttk.Checkbutton(frame, variable=var, text=text).pack(**args)
                else:
                    for t, v in zip(text, value):
                        ttk.Radiobutton(frame, variable=var, text=t, value=v).pack(**args)


if __name__ == "__main__":
    PaintBoard()
