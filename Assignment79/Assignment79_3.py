import tkinter as tk
import math

def calculate_area():
    try:
        radius = float(entry_radius.get())

        if radius < 0:
            result_label.config(text="Radius cannot be negative")
            return

        area = math.pi * radius ** 2
        result_label.config(text=f"Area of Circle = {area:.2f}")

    except ValueError:
        result_label.config(text="Please enter a valid radius")

root = tk.Tk()
root.title("Area of Circle")
root.geometry("350x220")

tk.Label(root, text="Enter Radius:").pack(pady=10)

entry_radius = tk.Entry(root)
entry_radius.pack()

tk.Button(
    root, text="Calculate Area", command=calculate_area
).pack(pady=10)

result_label = tk.Label(root, text="Area will appear here")
result_label.pack(pady=5)

root.mainloop()
