
import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x450")
root.minsize(300, 400)

display = tk.Entry(
    root,
    font=("Arial", 22),
    justify="right",
    bd=5
)
display.grid(row=0, column=0, columnspan=4,
             padx=10, pady=15, sticky="nsew")


def click(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))

    except ZeroDivisionError:
        clear()
        display.insert(0, "Cannot divide by zero")

    except Exception:
        clear()
        display.insert(0, "Invalid Input")


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for text, row, column in buttons:

    if text == "C":
        command = clear

    elif text == "=":
        command = calculate

    else:
        command = lambda value=text: click(value)

    button = tk.Button(
        root,
        text=text,
        font=("Arial", 18),
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5,
        sticky="nsew"
    )


for column in range(4):
    root.grid_columnconfigure(column, weight=1)

for row in range(5):
    root.grid_rowconfigure(row, weight=1)

root.mainloop()
