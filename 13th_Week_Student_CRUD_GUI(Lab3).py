import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

conn = sqlite3.connect("students_gui.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    department TEXT NOT NULL,
    semester TEXT NOT NULL
)
""")
conn.commit()

selected_id = None

root = tk.Tk()
root.title("Student CRUD System")
root.geometry("750x550")

form = tk.Frame(root, padx=10, pady=10)
form.pack(fill="x")

tk.Label(form, text="Name").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(form, width=35)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(form, text="Email").grid(row=1, column=0, sticky="w", pady=5)
email_entry = tk.Entry(form, width=35)
email_entry.grid(row=1, column=1, pady=5)

tk.Label(form, text="Department").grid(row=2, column=0, sticky="w", pady=5)
department_box = ttk.Combobox(
    form,
    values=["Computer Science", "Information Technology",
            "Software Engineering", "Computer Engineering"],
    state="readonly",
    width=32
)
department_box.grid(row=2, column=1, pady=5)

tk.Label(form, text="Semester").grid(row=3, column=0, sticky="w", pady=5)
semester_box = ttk.Combobox(
    form,
    values=["1", "2", "3", "4", "5", "6", "7", "8"],
    state="readonly",
    width=32
)
semester_box.grid(row=3, column=1, pady=5)

search_frame = tk.Frame(root, padx=10)
search_frame.pack(fill="x")

search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side="left", padx=5)

students_list = tk.Listbox(root, height=13, width=95)
students_list.pack(fill="both", expand=True, padx=10, pady=10)


def clear_form():
    global selected_id
    selected_id = None
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    department_box.set("")
    semester_box.set("")
    students_list.selection_clear(0, tk.END)


def show_students(search=""):
    students_list.delete(0, tk.END)
    cursor.execute(
        "SELECT id, name, email, department, semester FROM students "
        "WHERE name LIKE ? ORDER BY id",
        ("%" + search + "%",)
    )
    for student in cursor.fetchall():
        students_list.insert(
            tk.END,
            f"{student[0]} | {student[1]} | {student[2]} | "
            f"{student[3]} | Semester {student[4]}"
        )


def save_student():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    department = department_box.get()
    semester = semester_box.get()

    if not name or not email or not department or not semester:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        cursor.execute(
            "INSERT INTO students (name, email, department, semester) "
            "VALUES (?, ?, ?, ?)",
            (name, email, department, semester)
        )
        conn.commit()
        show_students(search_entry.get())
        clear_form()
        messagebox.showinfo("Success", "Student saved successfully.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Duplicate Email", "This email already exists.")


def select_student(event):
    global selected_id
    selection = students_list.curselection()

    if not selection:
        return

    record = students_list.get(selection[0])
    selected_id = int(record.split(" | ")[0])

    cursor.execute("SELECT * FROM students WHERE id = ?", (selected_id,))
    student = cursor.fetchone()

    if student:
        clear_entries_only()
        name_entry.insert(0, student[1])
        email_entry.insert(0, student[2])
        department_box.set(student[3])
        semester_box.set(student[4])
        selected_id = student[0]


def clear_entries_only():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    department_box.set("")
    semester_box.set("")


def update_student():
    if selected_id is None:
        messagebox.showerror("Error", "Please select a student first.")
        return

    name = name_entry.get().strip()
    email = email_entry.get().strip()
    department = department_box.get()
    semester = semester_box.get()

    if not name or not email or not department or not semester:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        cursor.execute(
            "UPDATE students SET name=?, email=?, department=?, semester=? "
            "WHERE id=?",
            (name, email, department, semester, selected_id)
        )
        conn.commit()
        show_students(search_entry.get())
        clear_form()
        messagebox.showinfo("Success", "Student updated successfully.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Duplicate Email", "This email already exists.")


def delete_student():
    if selected_id is None:
        messagebox.showerror("Error", "Please select a student first.")
        return

    answer = messagebox.askyesno(
        "Confirm Delete", "Are you sure you want to delete this student?"
    )

    if answer:
        cursor.execute("DELETE FROM students WHERE id = ?", (selected_id,))
        conn.commit()
        show_students(search_entry.get())
        clear_form()


def search_students():
    show_students(search_entry.get())


buttons = tk.Frame(root, pady=5)
buttons.pack()

tk.Button(buttons, text="Save", width=12, command=save_student).pack(side="left", padx=5)
tk.Button(buttons, text="Update", width=12, command=update_student).pack(side="left", padx=5)
tk.Button(buttons, text="Delete", width=12, command=delete_student).pack(side="left", padx=5)
tk.Button(buttons, text="Clear", width=12, command=clear_form).pack(side="left", padx=5)
tk.Button(search_frame, text="Search", command=search_students).pack(side="left", padx=5)
tk.Button(search_frame, text="Show All", command=lambda: (search_entry.delete(0, tk.END), show_students())).pack(side="left", padx=5)

students_list.bind("<<ListboxSelect>>", select_student)

show_students()

def close_app():
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()
