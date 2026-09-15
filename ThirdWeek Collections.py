scores = [15, 42, 8, 91, 23]

total_elements = len(scores)

lowest_val = min(scores)
highest_val = max(scores)

numeric_total = sum(scores)

ordered_list = sorted(scores)

are_all_truthy = all(scores)

print("Length:", total_elements)
print("Min:", lowest_val, "| Max:", highest_val)
print("Sum:", numeric_total)
print("Sorted Copy:", ordered_list)
print("All elements truthy?:", are_all_truthy)
