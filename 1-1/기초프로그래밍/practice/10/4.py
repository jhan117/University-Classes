"""
실습: 이미지 처리 프로그램에 기능 추가하기

앞서 설명한 이미지 처리 프로그램에 다음과 같은 기능을 추가하라.
- 왼쪽 마우스 버튼 클릭 시 원 그리기 기능을 컨트롤 키를 누른 상태에서 왼쪽 마우스 버튼 클릭 시(<Control-Button-1>) 원 그리기로 변경하라.
- 그림 위에 펜으로 그리기 : 왼쪽 마우스 버튼을 누른 상태에서 움직이면 그대로 그림이 그려지도록 만들어 보라.
한 가지 방법으로 마우스가 움직 일 때마다 이전 점에서 현재 점까지 직선을 그려주는 방법이 있다.
- [이미지 처리] 메뉴의 하위 메뉴로 [문자열 입력]을 추가하라.
[문자열 입력]을 실행하면 사용자로부터 문자열과 출력 좌표를 입력받아 이미지의 해당 위치에 문자열을 출력하라.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageDraw
from tkinter import messagebox as msgbox


image, tk_img = None, None
img_width, img_height, prev_pos = 0, 0, None
entry_text, entry_text_x, entry_text_y = None, None, None
filetypes = [("PNG", "*.png"), ("JPEG", "*.jpg")]


def show_img():
    """이미지 출력"""
    global tk_img

    if tk_img:
        canvas.delete(tk.ALL)
    tk_img = ImageTk.PhotoImage(image)

    canvas.create_image(canvas.winfo_width()/2, canvas.winfo_height()/2,
                        image=tk_img)


def find_pos(x, y, text_mode=False):
    if text_mode:
        return int(x), int(y)

    x -= canvas.winfo_width()/2 - img_width / 2
    y -= canvas.winfo_height()/2 - img_height / 2

    return x, y


def open_file():
    """파일 열기"""
    global image, img_width, img_height

    filename = filedialog.askopenfilename()
    if filename:
        image = Image.open(filename)
        img_width, img_height = image.size
        root.geometry(f"{img_width}x{img_height}")
        root.title(filename.split("/")[-1].split(".")[0])
        root.update()
        show_img()

        # show menus
        menubar.entryconfig("Image Processing", state=tk.NORMAL)
        menubar.entryconfig("Filter", state=tk.NORMAL)
        menu_file.entryconfig("Save", state=tk.NORMAL)


def save_file():
    """파일 저장"""
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=filetypes)
    if filename:
        image.save(filename)
        root.title(filename.split("/")[-1].split(".")[0])
        root.update()


def rotate_img(angle):
    global image

    image = image.rotate(angle, expand=True)
    show_img()


def transpose_img(option):
    global image

    image = image.transpose(option)
    show_img()


def filter_img(option):
    global image

    image = image.filter(option)
    show_img()


def draw_circle(e):
    x, y = find_pos(e.x, e.y)

    ImageDraw.Draw(image).ellipse([x - 10, y - 10, x + 10, y + 10], outline="white")
    show_img()


def resize(e):
    global image

    if image:
        show_img()


def press_button(e):
    global prev_pos

    prev_pos = e.x, e.y


def moving_mouse(e):
    global prev_pos

    if prev_pos:
        prev_x, prev_y = find_pos(*prev_pos)
        x, y = find_pos(e.x, e.y)
        ImageDraw.Draw(image).line([prev_x, prev_y, x, y], fill="blue", width=2)
        show_img()
        prev_pos = e.x, e.y


def release_mouse(e):
    global prev_pos

    prev_pos = None


def apply_text(window):
    text = entry_text.get()
    x = entry_text_x.get()
    y = entry_text_y.get()
    if not text or not x or not y:
        msgbox.showerror("입력 오류", "빈 곳이 없어야 합니다.")
        return
    elif not x.isdigit() or not y.isdigit():
        msgbox.showerror("입력 오류", "x, y는 숫자만 입력해야 합니다.")
        return
    ImageDraw.Draw(image).text(find_pos(x, y, text_mode=True), text, fill="Red", stroke_fill="Yellow", stroke_width=1, align="center")
    show_img()
    window.destroy()


def input_text():
    global entry_text, entry_text_x, entry_text_y

    text_root = tk.Toplevel(root)
    text_root.title("Input Text")

    ttk.Label(text_root, text="Input Text", anchor="center").pack(fill=tk.X, expand=True)
    entry_text = ttk.Entry(text_root)
    entry_text.pack(fill=tk.X, expand=True)
    ttk.Label(text_root, text="Enter Position(x, y)", anchor="center").pack(fill=tk.X, expand=True)
    left_frame = tk.Frame(text_root)
    right_frame = tk.Frame(text_root)
    left_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
    right_frame.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT)
    entry_text_x = ttk.Entry(left_frame)
    entry_text_x.pack(fill=tk.X, expand=True, side=tk.TOP)
    ttk.Button(left_frame, text="Apply",
               command=lambda: apply_text(text_root)).pack(fill=tk.X, expand=True, side=tk.BOTTOM)
    entry_text_y = ttk.Entry(right_frame)
    ttk.Button(right_frame, text="Cancel",
               command=lambda: text_root.destroy()).pack(fill=tk.X, expand=True, side=tk.BOTTOM)
    entry_text_y.pack(fill=tk.X, expand=True, side=tk.TOP)


root = tk.Tk()
root.option_add('*tearOff', tk.FALSE)   # 점선 제거

canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)
# == Menu Bar == #
menubar = tk.Menu(root)
root["menu"] = menubar
menu_file = tk.Menu(menubar)
menu_proc = tk.Menu(menubar)
menu_filter = tk.Menu(menubar)

# == Menu == #
menubar.add_cascade(menu=menu_file, label="File")
menubar.add_cascade(menu=menu_proc, label="Image Processing")
menubar.add_cascade(menu=menu_filter, label="Filter")
menubar.entryconfig("Image Processing", state=tk.DISABLED)
menubar.entryconfig("Filter", state=tk.DISABLED)

# == File Menu == #
menu_file_settings = {"Open": open_file, "Save": save_file, "Exit": lambda: root.quit()}
for label, command in menu_file_settings.items():
    menu_file.add_command(label=label, command=command)
menu_file.entryconfig("Save", state=tk.DISABLED)    # 열지 않으면 저장 금지

# == Img Proc Menu == #
menu_proc.add_command(label="90-Degree Rotation", command=lambda: rotate_img(90))
menu_proc.add_command(label="Horizontal Flip", command=lambda: transpose_img(Image.Transpose.FLIP_LEFT_RIGHT))
menu_proc.add_command(label="Input Text", command=input_text)

# == Filter Menu: Flt Img == #
menu_filter.add_command(label="Blur", command=lambda: filter_img(ImageFilter.BLUR))
menu_filter.add_command(label="Sharpen", command=lambda: filter_img(ImageFilter.SHARPEN))

# == event == #
canvas.bind("<ButtonPress-1>", press_button)
canvas.bind("<B1-Motion>", moving_mouse)
canvas.bind("<ButtonRelease-1>", release_mouse)
canvas.bind("<Control-Button-1>", draw_circle)
canvas.bind("<Configure>", resize)

root.mainloop()
