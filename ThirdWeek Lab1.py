scores = [85, 42, 90, 75, 42, 60, 95, 58, 88, 71]
student_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack"]
student_ids = [f"S{i:03d}" for i in range(1, 11)]

min_score = min(scores)
max_score = max(scores)
avg_score = sum(scores) / len(scores)

passing_scores = [s for s in scores if s >= 60]

unique_scores = set(scores)

student_dict = dict(zip(student_ids, student_names))

search_id = "S003"
found_student = student_dict.get(search_id, "Not Found")

all_records = list(zip(student_names, scores))
sorted_records = sorted(all_records, key=lambda x: x[1])

print("--- Statistics ---")
print(f"Min: {min_score} | Max: {max_score} | Average: {avg_score:.2f}")

print("\n--- Passing Scores (Comprehension) ---")
print(passing_scores)

print("\n--- Unique Scores (Set) ---")
print(unique_scores)

print("\n--- ID Mapping & Search ---")
print(f"Search for {search_id}: {found_student}")

print("\n--- Sorted Records by Score ---")
for rank, (name, score) in enumerate(sorted_records, start=1):
    print(f"Rank {rank}: {name} - {score}")
