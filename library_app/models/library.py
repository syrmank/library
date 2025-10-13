from .book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str) -> str:
        if any (book.title == title for book in self.books):
            return "Ошибка: книга уже существует"
        self.books.append(Book(title, author))
        return f"Книга '{title}' добавлена"
    
    def remove_book(self, title: str) -> str:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return f"Книга '{title}' удалена"
        return "Ошибка: книга не найдена"
    
    def find_book(self, title: str) -> str:
        for book in self.books:
            if book.title == title:
                return f"Книга '{book.title}' найдена"
            return "Книга не найдена"