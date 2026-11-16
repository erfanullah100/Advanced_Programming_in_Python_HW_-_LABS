
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Student Preferences Form")
root.geometry("500x700")

tk.Label(root, text="Student Preferences Form",
         font=("Arial", 18, "bold")).pack(pady=10)

details = tk.LabelFrame(root, text="Student Details", padx=10, pady=10)
details.pack(fill="x", padx=15, pady=5)

tk.Label(details, text="Student Name:").grid(row=0, column=0, pady=5)
name_entry = tk.Entry(details, width=30)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(details, text="Department:").grid(row=1, column=0, pady=5)
department = ttk.Combobox(
    details,
    values=["Computer Science", "Information Technology",
            "Software Engineering", "Computer Engineering"],
    state="readonly",
    width=27
)
department.grid(row=1, column=1, pady=5)
department.set("Computer Science")

study = tk.LabelFrame(root, text="Study Mode", padx=10, pady=10)
study.pack(fill="x", padx=15, pady=5)

mode = tk.StringVar(value="On-campus")

for option in ["On-campus", "Online", "Hybrid"]:
    tk.Radiobutton(study, text=option, variable=mode,
                   value=option).pack(anchor="w")

communication = tk.LabelFrame(root, text="Communication Preferences",
                              padx=10, pady=10)
communication.pack(fill="x", padx=15, pady=5)

email = tk.BooleanVar()
sms = tk.BooleanVar()
phone = tk.BooleanVar()

tk.Checkbutton(communication, text="Email", variable=email).pack(anchor="w")
tk.Checkbutton(communication, text="SMS", variable=sms).pack(anchor="w")
tk.Checkbutton(communication, text="Phone", variable=phone).pack(anchor="w")

experience = tk.LabelFrame(root, text="Programming Experience",
                           padx=10, pady=5)
experience.pack(fill="x", padx=15, pady=5)

level = tk.Scale(experience, from_=1, to=10, orient="horizontal")
level.set(5)
level.pack(fill="x")

skills_frame = tk.LabelFrame(root, text="Programming Skills",
                             padx=10, pady=10)
skills_frame.pack(fill="x", padx=15, pady=5)

skills_list = tk.Listbox(skills_frame, selectmode="multiple", height=5)
skills_list.pack(fill="x")

for skill in ["Python", "Java", "C++", "JavaScript",
              "HTML/CSS", "SQL", "PHP", "Kotlin"]:
    skills_list.insert(tk.END, skill)

summary = tk.Label(root, text="", justify="left", anchor="w")
summary.pack(fill="x", padx=20, pady=10)


def save():
    name = name_entry.get().strip()

    if not name:
        summary.config(text="Please enter student name.", fg="red")
        return

    contacts = []
    if email.get():
        contacts.append("Email")
    if sms.get():
        contacts.append("SMS")
    if phone.get():
        contacts.append("Phone")

    selected_skills = [
        skills_list.get(i) for i in skills_list.curselection()
    ]

    result = (
        f"Student Name: {name}\n"
        f"Department: {department.get()}\n"
        f"Study Mode: {mode.get()}\n"
        f"Communication: {', '.join(contacts) if contacts else 'None'}\n"
        f"Experience Level: {level.get()}\n"
        f"Skills: {', '.join(selected_skills) if selected_skills else 'None'}"
    )

    summary.config(text=result, fg="green")


tk.Button(root, text="Save Preferences",
          command=save, width=18).pack(pady=10)

root.mainloop()
