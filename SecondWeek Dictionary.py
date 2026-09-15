student = {"name": "Alice", "age": 20, "major": "CS"}

all_keys = list(student.keys())

all_values = list(student.values())

all_items = list(student.items())

email = student.get("email", "Not Found")

student.update({"age": 21, "gpa": 3.8})

removed_major = student.pop("major")

print("Keys:", all_keys)
print("Values:", all_values)
print("Items:", all_items)
print("Email lookup:", email)
print("Removed major:", removed_major)
print("Updated Dictionary:", student)
