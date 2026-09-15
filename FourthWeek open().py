with open("output.txt", "w") as file:
    file.write("Hello, Python File Handling!")

with open("output.txt", "r") as file:
    content = file.read()

print("File Content:", content)
