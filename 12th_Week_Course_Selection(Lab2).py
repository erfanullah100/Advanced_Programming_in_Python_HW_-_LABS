import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Course Selection")
root.geometry("450x500")

courses = [
    "Programming", "Advanced Programming", "Database Systems",
    "Computer Networks", "Operating Systems", "Web Development",
    "Data Structures", "Algorithms", "Software Engineering",
    "Computer Architecture", "Artificial Intelligence", "Cyber Security"
]

tk.Label(root, text="Course Selection", font=("Arial", 18, "bold")).pack(pady=10)

course_frame = tk.Frame(root)
course_frame.pack(padx=20, pady=10, fill="both", expand=True)

scrollbar = tk.Scrollbar(course_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

course_list = tk.Listbox(
    course_frame, selectmode="multiple",
    height=12, yscrollcommand=scrollbar.set
)
course_list.pack(side="left", fill="both", expand=True)
scrollbar.config(command=course_list.yview)

for course in courses:
    course_list.insert(tk.END, course)

semester = ttk.Combobox(
    root, values=["First", "Second", "Third", "Fourth", "Fifth", "Sixth"],
    state="readonly"
)
semester.set("First")
semester.pack(pady=10)

status = tk.Label(root, text="Selected courses: 0")
status.pack(pady=5)

summary = tk.Label(root, text="", justify="left")
summary.pack(pady=10)


def update_count(event=None):
    status.config(text=f"Selected courses: {len(course_list.curselection())}")


def show_selection():
    selected = [course_list.get(i) for i in course_list.curselection()]
    if selected:
        summary.config(text="Semester: " + semester.get() + "\nCourses: " + ", ".join(selected))
    else:
        summary.config(text="Please select at least one course.")


def clear_selection():
    course_list.selection_clear(0, tk.END)
    summary.config(text="Selection cleared.")
    update_count()


course_list.bind("<<ListboxSelect>>", update_count)

buttons = tk.Frame(root)
buttons.pack(pady=10)

tk.Button(buttons, text="Show Selection", command=show_selection).pack(side="left", padx=5)
tk.Button(buttons, text="Clear Selection", command=clear_selection).pack(side="left", padx=5)

root.mainloop()
