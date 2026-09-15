with open("sample.txt", "w+") as file:
    file.write("Python")

    initial_position = file.tell()

    file.seek(2)
    moved_position = file.tell()

    character = file.read(1)
    after_read_position = file.tell()

print(f"Position after writing 'Python': {initial_position}")
print(f"Position after seek(2): {moved_position}")
print(f"Read character: '{character}'")
print(f"Position after reading 1 character: {after_read_position}")
