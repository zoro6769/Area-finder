import tkinter as tk
from tkinter import messagebox
import math
root = tk.Tk()
root.title("Area finder")
root.geometry("400x350")
root.configure(bg = "#1f2f1f")
shape_var = tk.StringVar(value="Rectangle")
input_frame = tk.Frame(root, bg = "#1f2f1f")
input_frame.pack(pady = 10)
result_label = tk.Label(root, text = "", bg = "#1e1e2f", font=("Arial", 14, "bold"))
result_label.pack(pady = 5)
def update_fields(*args):
    for widget in input_frame.winfo_children():
        widget.destroy()
    if shape_var.get() == "Rectangle":
        tk.Label(input_frame, text = "Length", bg = "#2f1f1f", fg = "white").pack()
        global length_entry
        length_entry = tk.Entry(input_frame)
        length_entry.pack()

        tk.Label(input_frame, text = "Breadth", bg = "#2f1f1f", fg = "white").pack()
        global breadth_entry
        breadth_entry = tk.Entry(input_frame)
        breadth_entry.pack()

    elif shape_var.get() == "Square":
        tk.Label(input_frame, text = "side", bg = "#2f1f1f", fg = "white").pack()
        global side_entry 
        side_entry = tk.Entry(input_frame)
        side_entry.pack()

    elif shape_var.get() == "Triangle":
        tk.Label(input_frame, text = "Base", bg = "#2f1f1f", fg = "white").pack()
        global base_entry
        base_entry  = tk.Entry(input_frame)
        base_entry.pack()

        tk.Label(input_frame, text = "Height", bg = "#2f1f1f", fg = "white").pack()
        global height_entry
        height_entry = tk.Entry(input_frame)
        height_entry.pack()
    elif shape_var.get() == "Circle":
        tk.Label(input_frame, text = "Radius", bg = "#2f1f1f", fg = "white").pack()
        global radius_entry
        radius_entry = tk.Entry(input_frame)
        radius_entry.pack()
def calculation():
    try:
        selected = shape_var.get()
        if selected == "Rectangle":
            area = float(length_entry.get()) * float(breadth_entry.get())
        elif selected == "Square":
            area = float(side_entry.get()) * float(side_entry.get())
        elif selected == "Triangle":
            area = float(base_entry.get()) * float(height_entry.get()) * 0.5
        elif selected == "Circle":
            area = math.pi * float(radius_entry.get()) * float(radius_entry.get())
        else:
            return
        result_label.config(text=f"Area = {area:.2f}")
    except:
        messagebox.showerror("Invalid input. Enter valid numbers!")
tk.Label(root, text = "Area Finder", bg = "#2f1e1e", fg = "white", font=("Arial", 14, "bold")).pack(pady = 10)
tk.Label(root, text = "Choose your shape", bg = "#2f1e1e", fg = "white", font=("Arial", 14, "bold")).pack()
options = ["Rectangle", "Square", "Triangle", "Circle"]
menu = tk.OptionMenu(root, shape_var, *options)
menu.pack(pady = 5)

shape_var.trace_add("write", update_fields)

def on_enter(e):
    e.widget.config(bg = "#a04549")
def on_leave(e):
    e.widget.config(bg="#4549a0")
calc_btn = tk.Button(root, text = "Calculate", command=calculation, bg = "#4549a0", fg = "white", font=("Arial", 14, "bold"), relief="flat")
calc_btn.pack(pady = 10)
calc_btn.bind("<Enter>", on_enter)
calc_btn.bind("<Leave>", on_leave)
update_fields()
root.mainloop()