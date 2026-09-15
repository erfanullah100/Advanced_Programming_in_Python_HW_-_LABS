from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email address format.")
        self._email = value

    @abstractmethod
    def role_info(self):
        pass

    def __str__(self):
        return f"{self.name} ({self.email})"


class Student(Person):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id

    def role_info(self):
        return f"Student ID: {self.student_id}"

    def __str__(self):
        return f"Student: {super().__str__()} | {self.role_info()}"


class Lecturer(Person):
    def __init__(self, name, email, employee_id):
        super().__init__(name, email)
        self.employee_id = employee_id

    def role_info(self):
        return f"Employee ID: {self.employee_id}"

    def __str__(self):
        return f"Lecturer: {super().__str__()} | {self.role_info()}"


class Course:
    def __init__(self, course_name, lecturer):
        self.course_name = course_name
        self.lecturer = lecturer
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)

    def __str__(self):
        student_names = ", ".join([s.name for s in self.students])
        return f"Course: {self.course_name} | Instructor: {self.lecturer.name} | Enrolled: [{student_names}]"


if __name__ == "__main__":
    lecturer = Lecturer("Dr. Alice Smith", "alice.smith@uni.edu", "L9872")
    student1 = Student("John Doe", "john.doe@student.com", "S1001")
    student2 = Student("Jane Miller", "jane.m@student.com", "S1002")

    oop_course = Course("Object-Oriented Programming", lecturer)
    oop_course.add_student(student1)
    oop_course.add_student(student2)

    print("--- Course Composition Details ---")
    print(oop_course)

    print("\n--- Polymorphic Printing ---")
    people_list = [lecturer, student1, student2]

    for person in people_list:
        print(f"Name: {person.name} | Role Details: {person.role_info()}")
