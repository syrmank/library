books = []

def add_book(title: str, author: str) -> str:
    if not title or not author:
        return "Ошибка: некорректные данные"
    for book in books:
        if book == title:
            return f"Ошибка: книга уже существует"
    books.append(title)
    return f"Книга '{title}' добавлена"