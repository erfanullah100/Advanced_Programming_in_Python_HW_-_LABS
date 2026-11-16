import tkinter as tk

root = tk.Tk()
root.title("Keyboard Event Viewer")
root.geometry("650x450")


def key_pressed(event):
    key_label.config(
        text=f"Last Key Pressed: {event.keysym}"
    )

    keysym_label.config(
        text=f"event.keysym = {event.keysym}"
    )

    char_label.config(
        text=f"event.char = {repr(event.char)}"
    )

    if root.focus_get() == text_entry:
        focus_label.config(text="Keyboard Focus: Entry")
    else:
        focus_label.config(text="Keyboard Focus: Root Window")


def clear_display(event=None):
    key_label.config(text="Last Key Pressed: None")
    keysym_label.config(text="event.keysym = None")
    char_label.config(text="event.char = None")
    status_label.config(text="Status: Display cleared")


def save(event=None):
    status_label.config(text="Status: Saved")
    return "break"


title_label = tk.Label(
    root,
    text="Keyboard Event Viewer",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=15)


key_label = tk.Label(
    root,
    text="Last Key Pressed: None",
    font=("Arial", 15)
)
key_label.pack(pady=10)


keysym_label = tk.Label(
    root,
    text="event.keysym = None",
    font=("Arial", 12)
)
keysym_label.pack(pady=5)


char_label = tk.Label(
    root,
    text="event.char = None",
    font=("Arial", 12)
)
char_label.pack(pady=5)


entry_label = tk.Label(
    root,
    text="Click inside the Entry and type:"
)
entry_label.pack(pady=(20, 5))


text_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 14)
)
text_entry.pack(pady=5)


focus_label = tk.Label(
    root,
    text="Keyboard Focus: Root Window",
    font=("Arial", 11)
)
focus_label.pack(pady=10)


status_label = tk.Label(
    root,
    text="Status: Ready",
    font=("Arial", 12, "bold")
)
status_label.pack(pady=10)


shortcut_label = tk.Label(
    root,
    text="Escape = Clear    |    Ctrl + S = Save"
)
shortcut_label.pack(pady=10)


root.bind("<KeyPress>", key_pressed)
root.bind("<Escape>", clear_display)
root.bind("<Control-s>", save)

root.focus_set()

root.mainloop()