import tkinter as tk

root = tk.Tk()
root.title("Keyboard Controlled Player")
root.geometry("500x400")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

player = canvas.create_rectangle(50, 50, 90, 90, fill="blue")

status = tk.Label(root, text="X: 70  Y: 70")
status.pack()


def move(event):
    speed = 20

    if event.keysym == "Shift_L":
        speed = 40

    if event.keysym == "Up":
        canvas.move(player, 0, -speed)
    elif event.keysym == "Down":
        canvas.move(player, 0, speed)
    elif event.keysym == "Left":
        canvas.move(player, -speed, 0)
    elif event.keysym == "Right":
        canvas.move(player, speed, 0)

    x1, y1, x2, y2 = canvas.coords(player)

    if x1 < 0:
        canvas.move(player, -x1, 0)
    if y1 < 0:
        canvas.move(player, 0, -y1)
    if x2 > 500:
        canvas.move(player, 500 - x2, 0)
    if y2 > 400:
        canvas.move(player, 0, 400 - y2)

    x1, y1, x2, y2 = canvas.coords(player)
    status.config(text=f"X: {(x1+x2)/2:.0f}  Y: {(y1+y2)/2:.0f}")


def reset(event):
    canvas.coords(player, 50, 50, 90, 90)
    status.config(text="X: 70  Y: 70")


root.bind("<Key>", move)
root.bind("<r>", reset)
root.bind("<R>", reset)

root.mainloop()