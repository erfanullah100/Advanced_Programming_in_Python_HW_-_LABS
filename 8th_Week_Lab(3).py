import tkinter as tk

root = tk.Tk()
root.title("Event-Driven Login Form")
root.geometry("500x400")


def validate_form():

    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "":
        return False, "Username cannot be empty."

    if password == "":
        return False, "Password cannot be empty."

    if len(password) < 4:
        return False, "Password must contain at least 4 characters."

    return True, "Validation successful."


def login(event=None):

    valid, message = validate_form()

    if not valid:
        status_label.config(text=message)
        return

    username = username_entry.get().strip()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        status_label.config(text="Login successful!")
    else:
        status_label.config(
            text="Invalid username or password."
        )


def clear_form(event=None):

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    status_label.config(text="Form cleared.")

    username_entry.focus_set()


def field_focus_in(event):

    if event.widget == username_entry:
        active_label.config(
            text="Active Field: Username"
        )

    elif event.widget == password_entry:
        active_label.config(
            text="Active Field: Password"
        )


def field_focus_out(event):
    active_label.config(text="Active Field: None")


title_label = tk.Label(
    root,
    text="Event-Driven Login Form",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)


form_frame = tk.Frame(root)
form_frame.pack(pady=10)


username_label = tk.Label(
    form_frame,
    text="Username:",
    font=("Arial", 12)
)
username_label.grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)


username_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12)
)
username_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)


password_label = tk.Label(
    form_frame,
    text="Password:",
    font=("Arial", 12)
)
password_label.grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)


password_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12),
    show="*"
)
password_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)


login_button = tk.Button(
    root,
    text="Login",
    command=login,
    width=15,
    font=("Arial", 12)
)
login_button.pack(pady=15)


active_label = tk.Label(
    root,
    text="Active Field: None",
    font=("Arial", 11)
)
active_label.pack(pady=5)


status_label = tk.Label(
    root,
    text="Enter username and password.",
    font=("Arial", 11, "bold")
)
status_label.pack(pady=10)


shortcut_label = tk.Label(
    root,
    text="Enter = Login    |    Escape = Clear"
)
shortcut_label.pack(pady=10)


root.bind("<Return>", login)
root.bind("<Escape>", clear_form)

username_entry.bind("<FocusIn>", field_focus_in)
username_entry.bind("<FocusOut>", field_focus_out)

password_entry.bind("<FocusIn>", field_focus_in)
password_entry.bind("<FocusOut>", field_focus_out)


username_entry.focus_set()

root.mainloop()