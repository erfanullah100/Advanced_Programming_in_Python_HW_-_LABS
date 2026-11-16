import tkinter as tk

root = tk.Tk()
root.title("Bouncing Ball")
root.geometry("500x400")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

ball = canvas.create_oval(50, 50, 90, 90, fill="red")

dx = 3
dy = 3
running = False
speed = 20


def animate():
    global dx, dy

    if running:
        canvas.move(ball, dx, dy)

        x1, y1, x2, y2 = canvas.coords(ball)

        if x1 <= 0 or x2 >= 500:
            dx = -dx

        if y1 <= 0 or y2 >= 400:
            dy = -dy

        root.after(speed, animate)


def start():
    global running
    if not running:
        running = True
        animate()


def pause():
    global running
    running = False


def reset():
    global running, dx, dy
    running = False
    dx = 3
    dy = 3
    canvas.coords(ball, 50, 50, 90, 90)


def faster():
    global dx, dy
    dx *= 1.5
    dy *= 1.5


def slower():
    global dx, dy
    dx *= 0.7
    dy *= 0.7


buttons = tk.Frame(root)
buttons.pack(pady=10)

tk.Button(buttons, text="Start", command=start).pack(side="left", padx=5)
tk.Button(buttons, text="Pause", command=pause).pack(side="left", padx=5)
tk.Button(buttons, text="Reset", command=reset).pack(side="left", padx=5)
tk.Button(buttons, text="Faster", command=faster).pack(side="left", padx=5)
tk.Button(buttons, text="Slower", command=slower).pack(side="left", padx=5)

root.mainloop()