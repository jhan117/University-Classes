import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random


def create_circles():
    try:
        circles.clear()
        canvas.delete(tk.ALL)
        num = int(num_input.get())
        for _ in range(num):
            random_x = random.randint(*x_range)
            random_y = random.randint(*y_range)
            random_r = random.randint(*r_range)
            random_c = random.choice(colors)
            circles.append([random_x, random_y, random_r, random_c])
            canvas.create_oval(random_x - random_r, random_y - random_r,
                               random_x + random_r, random_y + random_r, outline=random_c)
        num_input.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Error: Please enter a number")


def save_file():
    with open("resources/circles.txt", "w") as file:
        for circle in circles:
            file.write(" ".join(str(c) for c in circle))
            file.write("\n")


def delete_circles():
    circles.clear()
    canvas.delete(tk.ALL)


def read_file():
    try:
        with open("resources/circles.txt", "r") as file:
            for line in file:
                data = [int(d) if d.isnumeric() else d for d in line.split()]
                [x, y, r, c] = data
                circles.append(data)
                canvas.create_oval(x - r, y - r,
                                   x + r, y + r, outline=c)
    except FileNotFoundError:
        messagebox.showerror("Error", "Error: File Not Found")


# == init == #
# variables
circles = []
x_range = (50, 550)
y_range = (50, 350)
r_range = (10, 50)
colors = ["red", "blue", "green"]
# window
root = tk.Tk()
root.title("Make Circles")
# == main == #
canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
# == footer == #
footer = ttk.Frame(root)
footer.pack(side=tk.BOTTOM, fill=tk.X, padx=3, pady=3)
# footer widgets
num_input = ttk.Entry(footer)
ttk.Button(footer, text="Read A File", command=read_file).pack(side=tk.RIGHT)
ttk.Button(footer, text="Delete Circles", command=delete_circles).pack(side=tk.RIGHT)
ttk.Button(footer, text="Save A File", command=save_file).pack(side=tk.RIGHT)
ttk.Button(footer, text="Create New Circles", command=create_circles).pack(side=tk.RIGHT)
num_input.pack(side=tk.LEFT, fill=tk.X, expand=True)

root.mainloop()
