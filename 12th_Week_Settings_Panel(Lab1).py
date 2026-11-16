import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Settings Panel")
root.geometry("450x550")

email = tk.BooleanVar()
sms = tk.BooleanVar()
desktop = tk.BooleanVar()
theme = tk.StringVar(value="System")

tk.Label(root, text="Settings Panel", font=("Arial", 18, "bold")).pack(pady=10)

notifications = tk.LabelFrame(root, text="Notifications", padx=10, pady=10)
notifications.pack(fill="x", padx=20, pady=8)

tk.Checkbutton(notifications, text="Email", variable=email).pack(anchor="w")
tk.Checkbutton(notifications, text="SMS", variable=sms).pack(anchor="w")
tk.Checkbutton(notifications, text="Desktop", variable=desktop).pack(anchor="w")

themes = tk.LabelFrame(root, text="Theme", padx=10, pady=10)
themes.pack(fill="x", padx=20, pady=8)

for option in ["Light", "Dark", "System"]:
    tk.Radiobutton(themes, text=option, variable=theme, value=option).pack(anchor="w")

tk.Label(root, text="Notification Volume").pack(pady=5)
volume = tk.Scale(root, from_=0, to=100, orient="horizontal")
volume.set(50)
volume.pack(fill="x", padx=30)

tk.Label(root, text="Language").pack(pady=5)
language = ttk.Combobox(root, values=["English", "Pashto", "Dari"], state="readonly")
language.set("English")
language.pack()

summary = tk.Label(root, text="Your settings will appear here.", justify="left")
summary.pack(pady=15)


def save():
    text = (
        f"Email: {email.get()}\nSMS: {sms.get()}\n"
        f"Desktop: {desktop.get()}\nTheme: {theme.get()}\n"
        f"Volume: {volume.get()}\nLanguage: {language.get()}"
    )
    summary.config(text=text)


def reset():
    email.set(False)
    sms.set(False)
    desktop.set(False)
    theme.set("System")
    volume.set(50)
    language.set("English")
    summary.config(text="Settings reset.")


buttons = tk.Frame(root)
buttons.pack(pady=10)

tk.Button(buttons, text="Save", width=12, command=save).pack(side="left", padx=5)
tk.Button(buttons, text="Reset", width=12, command=reset).pack(side="left", padx=5)

root.mainloop()
