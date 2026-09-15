numbers = {1, 2, 2, 3, 4}

numbers.add(5)
numbers.remove(3)

is_present = 4 in numbers

even_numbers = {2, 4, 6}
union_set = numbers.union(even_numbers)
intersection_set = numbers.intersection(even_numbers)

immutable_set = frozenset([10, 20, 30])

print("Set:", numbers)
print("Is 4 present?:", is_present)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Frozenset:", immutable_set)
