from typing import List


class NotFoundError(Exception):
    pass


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page) -> None:
        self.page = page


class Library:
    def __init__(self, books):
        self.books: List[Book] = books

    def find_book(self, title) -> "Book" | str:
        b = next((b for b in self.books if b.title == title), None)
        if b:
            return b
        raise NotFoundError(f"Book with {title} not found.")

    def register_book(self, book: "Book") -> None:
        self.books.append(book)
