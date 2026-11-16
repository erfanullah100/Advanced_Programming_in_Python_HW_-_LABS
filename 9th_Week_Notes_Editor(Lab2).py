
import tkinter as tk

root = tk.Tk()
root.title("Notes Editor")
root.geometry("600x500")

header = tk.Frame(root, bg="lightblue", pady=10)
header.pack(fill="x")

tk.Label(header, text="My Notes Editor",
         font=("Arial", 20, "bold"), bg="lightblue").pack()

text_area = tk.Text(root, font=("Arial", 12))
text_area.pack(fill="both", expand=True, padx=10, pady=10)

status = tk.Label(root, text="Ready")
status.pack(pady=5)


def clear():
    text_area.delete("1.0", tk.END)
    status.config(text="Notes cleared")


def sample():
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, "Welcome to Notes Editor!")
    status.config(text="Sample text inserted")


def toggle():
    state = text_area.cget("state")
    text_area.config(state="disabled" if state == "normal" else "normal")
    status.config(text="Editor status changed")


def save():
    with open("notes.txt", "w") as file:
        file.write(text_area.get("1.0", tk.END))
    status.config(text="Notes saved")


actions = tk.Frame(root)
actions.pack(pady=10)

tk.Button(actions, text="Clear", command=clear).pack(side="left", padx=5)
tk.Button(actions, text="Sample", command=sample).pack(side="left", padx=5)
tk.Button(actions, text="Disable/Enable", command=toggle).pack(side="left", padx=5)
tk.Button(actions, text="Save", command=save).pack(side="left", padx=5)

root.mainloop()
