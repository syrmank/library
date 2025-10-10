from library_app.main import add_book, books

def setup_function():
    books.clear()

def test_add_book_positive():
    """Проверяем корректное добавление книги"""
    result = add_book("1984", "Оруэлл")
    assert result == "Книга '1984' добавлена"

def test_add_book_duplicate():
    """Проверяем, что дубликаты не добавляются"""
    add_book("1984", "Оруэлл")
    result = add_book("1984", "Оруэлл")
    assert result == "Ошибка: книга уже существует"

def test_add_book_invalid():
    """Проверяем реакцию на неверные данные"""
    result = add_book("", "")
    assert result == "Ошибка: некорректные данные"