print("Library system started")


def add_book(title: str, author: str) -> None:
    """
    Добавляет книгу в библиотеку.

    :param title: Название книги
    :param author: Автор книги
    """
    print(f"Adding book {title} by {author}")


add_book("1986", "Orwell")
