class Book:
    # 1. __init__:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    # 2. __str__:
    def __str__(self):
        return f"'{self.title}'"

    # 3. __repr__:
    def __repr__(self):
        return f"Book(title='{self.title}', pages={self.pages})"

    # 4. __eq__:
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.pages == other.pages

    # 5. __len__:
    def __len__(self):
        return self.pages

    # 6. __lt__:
    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages



book1 = Book("Python Basics", 150)
book2 = Book("Advanced Python", 300)
book3 = Book("Python Basics", 150)

print(f"User string: {book1}")

print(f"Developer repr: {repr(book1)}")

print(f"Is book1 equal to book3? {book1 == book3}")

print(f"Length of book2: {len(book2)} pages")

print(f"Is book1 smaller than book2? {book1 < book2}")
