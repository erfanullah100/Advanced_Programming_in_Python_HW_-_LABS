from typing import Dict, Set, Union, Tuple

students: Dict[str, Dict[str, Union[str, Set[str]]]] = {
    "S001": {"name": "Alice", "courses": {"CS101", "MATH201"}},
    "S002": {"name": "Bob", "courses": {"CS101", "PHYS101"}},
    "S003": {"name": "Charlie", "courses": {"MATH201", "CHEM101"}}
}

students["S001"]["courses"].add("CS102")
students["S001"]["courses"].add("CS101")

students["S002"]["courses"].discard("PHYS101")

common_courses: Set[str] = students["S001"]["courses"].intersection(students["S002"]["courses"])

all_courses: Set[str] = set()
for record in students.values():
    all_courses = all_courses.union(record["courses"])

print("--- Updated Student Database ---")
for s_id, data in students.items():
    print(f"ID: {s_id} | Name: {data['name']} | Courses: {data['courses']}")

print("\n--- Set Operations ---")
print(f"Common courses between S001 and S002: {common_courses}")
print(f"All unique courses in system: {all_courses}")
