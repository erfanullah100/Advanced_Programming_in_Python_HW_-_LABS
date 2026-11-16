
import tkinter as tk

root = tk.Tk()
root.title("Student Profile Form")
root.geometry("500x600")
root.minsize(450, 550)

header = tk.Frame(root, bg="lightblue", pady=20)
header.pack(fill="x")

title = tk.Label(
    header,
    text="Student Profile Form",
    font=("Arial", 20, "bold"),
    bg="lightblue"
)
title.pack()

form = tk.Frame(root, padx=30, pady=20)
form.pack(fill="both", expand=True)

tk.Label(form, text="Full Name:").grid(row=0, column=0, pady=10, sticky="w")
name_entry = tk.Entry(form, width=30)
name_entry.grid(row=0, column=1, pady=10)

tk.Label(form, text="Student ID:").grid(row=1, column=0, pady=10, sticky="w")
id_entry = tk.Entry(form, width=30)
id_entry.grid(row=1, column=1, pady=10)

tk.Label(form, text="Email:").grid(row=2, column=0, pady=10, sticky="w")
email_entry = tk.Entry(form, width=30)
email_entry.grid(row=2, column=1, pady=10)

tk.Label(form, text="Phone:").grid(row=3, column=0, pady=10, sticky="w")
phone_entry = tk.Entry(form, width=30)
phone_entry.grid(row=3, column=1, pady=10)

tk.Label(form, text="Address:").grid(row=4, column=0, pady=10, sticky="nw")
address_text = tk.Text(form, width=30, height=5)
address_text.grid(row=4, column=1, pady=10)


def save_data():
    name = name_entry.get()
    student_id = id_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_text.get("1.0", tk.END).strip()

    if not name or not student_id or not email or not phone or not address:
        status_label.config(text="Please fill in all fields.", fg="red")
    else:
        status_label.config(text="Profile saved successfully!", fg="green")


def clear_data():
    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_text.delete("1.0", tk.END)
    status_label.config(text="Form cleared.", fg="blue")


actions = tk.Frame(root, pady=10)
actions.pack()

save_button = tk.Button(actions, text="Save", width=12, command=save_data)
save_button.pack(side="left", padx=10)

clear_button = tk.Button(actions, text="Clear", width=12, command=clear_data)
clear_button.pack(side="left", padx=10)

status_label = tk.Label(root, text="", font=("Arial", 11))
status_label.pack(pady=10)

root.mainloop()
