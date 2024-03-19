from enum import Enum
from typing import List

class Status(Enum):
    AVAILABLE = "Available"
    BORROWED = "Borrowed"
    MAINTENANCE = "Maintenance"

class Book:
    def __init__(self, title: str, author: 'Author', category: 'Category', status: Status = Status.AVAILABLE):
        self.title = title
        self.author = author
        self.category = category
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author.name} in {self.category.name}, Status: {self.status.value}"

class Author:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

class Category:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        self.books = [book for book in self.books if book.title != title]

    def find_books_by_author(self, author_name: str) -> List[Book]:
        return [book for book in self.books if book.author.name == author_name]

# Példa használatra, beleértve a könyvtár adatbázisának bővítését további könyvekkel
if __name__ == "__main__":
    # Szerzők és kategóriák létrehozása
    authors = [
        Author("J.K. Rowling"),
        Author("George R.R. Martin"),
        Author("J.R.R. Tolkien"),
        Author("Isaac Asimov"),
        Author("Arthur C. Clarke"),
        Author("Stephen King"),
        Author("Agatha Christie"),
        Author("Douglas Adams"),
        Author("Neil Gaiman"),
        Author("Frank Herbert"),
        Author("Orson Scott Card")
    ]

    categories = [
        Category("Fantasy"),
        Category("Science Fiction"),
        Category("Horror"),
        Category("Mystery")
    ]

    # Könyvek hozzáadása
    books = [
        Book("Harry Potter and the Philosopher's Stone", authors[0], categories[0]),
        Book("A Game of Thrones", authors[1], categories[0]),
        Book("The Fellowship of the Ring", authors[2], categories[0]),
        Book("Foundation", authors[3], categories[1]),
        Book("2001: A Space Odyssey", authors[4], categories[1]),
        Book("The Shining", authors[5], categories[2]),
        Book("Murder on the Orient Express", authors[6], categories[3]),
        Book("The Hitchhiker's Guide to the Galaxy", authors[7], categories[1]),
        Book("American Gods", authors[8], categories[0]),
        Book("Dune", authors[9], categories[1]),
        Book("Ender's Game", authors[10], categories[1])
    ]

    library = Library()
    for book in books:
        library.add_book(book)

    # Könyvtárban lévő összes könyv kiíratása
    print("Library books:")
    for book in library.books:
        print(book)

    # Egy adott szerző könyveinek keresése és kiíratása
    print("\nBooks by Isaac Asimov:")
    for book in library.find_books_by_author("Isaac Asimov"):
        print(book)
