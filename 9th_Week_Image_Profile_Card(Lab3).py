import tkinter as tk

root = tk.Tk()
root.title("Profile Card")
root.geometry("400x560")
root.resizable(False, False)

card = tk.Frame(root, padx=25, pady=20, bd=2, relief="groove")
card.pack(pady=20)

image = tk.PhotoImage(file="profile.png")
image = image.subsample(4, 4)

image_label = tk.Label(card, image=image)
image_label.pack(pady=10)

name_label = tk.Label(card, text="Erfanullah Ahmadi",
                      font=("Arial", 18, "bold"))
name_label.pack(pady=8)

department_label = tk.Label(card, text="Department: Computer Science",
                            font=("Arial", 12))
department_label.pack(pady=5)

email_label = tk.Label(card, text="Email: student@gmail.com",
                       font=("Arial", 11))
email_label.pack(pady=5)


def edit_profile():
    name_label.config(text="Name: Edited")
    department_label.config(text="Department: Updated")
    email_label.config(text="Email: updated@gmail.com")


buttons = tk.Frame(card)
buttons.pack(pady=15)

tk.Button(buttons, text="Edit", width=10,
          command=edit_profile).pack(side="left", padx=10)

tk.Button(buttons, text="Close", width=10,
          command=root.destroy).pack(side="left", padx=10)

root.mainloop()
