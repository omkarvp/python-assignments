import tkinter as tk

def find_maximum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())

        largest = max(num1, num2, num3)
        result_label.config(text=f"Largest Number = {largest}")

    except ValueError:
        result_label.config(text="Please enter valid numbers")

root = tk.Tk()
root.title("Find Largest Number")
root.geometry("350x300")

tk.Label(root, text="Enter First Number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Enter Third Number:").pack(pady=5)
entry3 = tk.Entry(root)
entry3.pack()

tk.Button(
    root, text="Find Maximum", command=find_maximum
).pack(pady=10)

result_label = tk.Label(root, text="Result will appear here")
result_label.pack(pady=5)

root.mainloop()