from models import Library

def main():
    lib = Library()
    print(lib.add_book("1984","Оруээлл"))
    print(lib.find_book("1984"))

if __name__ == "__main__":
    main()