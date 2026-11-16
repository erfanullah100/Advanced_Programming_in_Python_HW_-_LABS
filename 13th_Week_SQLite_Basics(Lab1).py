import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    semester INTEGER NOT NULL
)
""")

students = [
    ("Ahmad", "Computer Science", 1),
    ("Sara", "Information Technology", 2),
    ("Ali", "Software Engineering", 3),
    ("Maryam", "Computer Science", 4),
    ("Omar", "Information Technology", 2)
]

cursor.executemany(
    "INSERT INTO students (name, department, semester) VALUES (?, ?, ?)",
    students
)
conn.commit()

print("All students:")
cursor.execute("SELECT * FROM students")
for student in cursor.fetchall():
    print(student)

semester = 2
print("\nStudents in semester", semester)
cursor.execute("SELECT * FROM students WHERE semester = ?", (semester,))
for student in cursor.fetchall():
    print(student)

cursor.execute(
    "UPDATE students SET department = ? WHERE id = ?",
    ("Software Engineering", 1)
)
conn.commit()

cursor.execute("DELETE FROM students WHERE id = ?", (5,))
conn.commit()

print("\nFinal table contents:")
cursor.execute("SELECT * FROM students")
for student in cursor.fetchall():
    print(student)

conn.close()
