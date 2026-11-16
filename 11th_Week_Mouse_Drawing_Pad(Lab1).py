
import tkinter as tk

root = tk.Tk()
root.title("Mouse Drawing Pad")
root.geometry("600x500")

brush_size = 3

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)


def draw(event):
    r = brush_size
    canvas.create_oval(
        event.x-r, event.y-r,
        event.x+r, event.y+r,
        fill="black", outline="black"
    )
    status.config(text=f"X: {event.x}  Y: {event.y}")


def erase(event):
    canvas.create_oval(
        event.x-10, event.y-10,
        event.x+10, event.y+10,
        fill="white", outline="white"
    )


def clear():
    canvas.delete("all")
    status.config(text="Canvas cleared")


canvas.bind("<B1-Motion>", draw)
canvas.bind("<Motion>", lambda event: status.config(
    text=f"X: {event.x}  Y: {event.y}"
))
canvas.bind("<Button-3>", erase)

status = tk.Label(root, text="Ready")
status.pack(pady=5)

tk.Button(root, text="Clear", command=clear).pack(pady=5)

root.mainloop()
