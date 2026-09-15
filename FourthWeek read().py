with open("sample.txt", "w+") as file:
    file.write("DataScience")

    file.seek(0)
    pos_start = file.tell()

    part1 = file.read(4)
    pos_after_part1 = file.tell()

    part2 = file.read(7)
    pos_after_part2 = file.tell()

print(f"Starting cursor position: {pos_start}")
print(f"Read first 4 chars ('{part1}'): cursor moved to {pos_after_part1}")
print(f"Read next 7 chars ('{part2}'): cursor moved to {pos_after_part2}")
