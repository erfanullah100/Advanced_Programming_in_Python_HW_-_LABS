with open("sample.txt", "w+") as file:
    file.write("Python Programming")

    file.seek(7)

    content_from_position = file.read()
    print("Content from position 7 onwards:", content_from_position)

    file.seek(0)

    full_content = file.read()
    print("Full content from beginning:", full_content)
