from library_app.main import add_book

def test_add_book():
    assert add_book("1984", "Orwell") is None
    assert add_book("12341","1234") is None