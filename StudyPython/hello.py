import tkinter as tk
from math import pi

def calculate_area():
    radius = float(entry.get())
    area = pi * radius ** 2
    result_label.config(text=f"면적: {area:.2f}")

def calculate_circumference():
    radius = float(entry.get())
    circumference = 2 * pi * radius
    result_label.config(text=f"둘레: {circumference:.2f}")

window = tk.Tk()
window.title("원의 면적 및 둘레 계산기")

label = tk.Label(window, text="반지름")
label.pack()

entry = tk.Entry(window)
entry.pack()

area_button = tk.Button(window, text="면적 계산", command=calculate_area)
area_button.pack()

circumference_button = tk.Button(window, text="둘레 계산", command=calculate_circumference)
circumference_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
