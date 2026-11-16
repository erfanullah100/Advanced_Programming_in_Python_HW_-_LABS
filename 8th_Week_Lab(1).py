import tkinter as tk

root = tk.Tk()
root.title("Mouse Event Tracker")
root.geometry("650x450")

double_click_count = 0


def mouse_motion(event):
    position_label.config(
        text=f"Mouse Position: X = {event.x}, Y = {event.y}"
    )


def left_click(event):
    click_label.config(text="Action: Left Click")


def double_click(event):
    global double_click_count
    double_click_count += 1

    double_click_label.config(
        text=f"Double Clicks: {double_click_count}"
    )


def mouse_enter(event):
    status_label.config(text="Status: Mouse entered the frame")


def mouse_leave(event):
    status_label.config(text="Status: Mouse left the frame")


title_label = tk.Label(
    root,
    text="Mouse Event Tracker",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)


mouse_frame = tk.Frame(
    root,
    width=550,
    height=250,
    bg="lightblue",
    bd=3,
    relief="ridge"
)
mouse_frame.pack(pady=10)

mouse_frame.pack_propagate(False)


instruction_label = tk.Label(
    mouse_frame,
    text="Move and click your mouse inside this area",
    bg="lightblue",
    font=("Arial", 14)
)
instruction_label.place(relx=0.5, rely=0.5, anchor="center")


position_label = tk.Label(
    root,
    text="Mouse Position: X = 0, Y = 0",
    font=("Arial", 12)
)
position_label.pack(pady=3)


click_label = tk.Label(
    root,
    text="Action: None",
    font=("Arial", 12)
)
click_label.pack(pady=3)


double_click_label = tk.Label(
    root,
    text="Double Clicks: 0",
    font=("Arial", 12)
)
double_click_label.pack(pady=3)


status_label = tk.Label(
    root,
    text="Status: Waiting...",
    font=("Arial", 12, "bold")
)
status_label.pack(pady=5)


mouse_frame.bind("<Motion>", mouse_motion)
mouse_frame.bind("<Button-1>", left_click)
mouse_frame.bind("<Double-Button-1>", double_click)
mouse_frame.bind("<Enter>", mouse_enter)
mouse_frame.bind("<Leave>", mouse_leave)

root.mainloop()