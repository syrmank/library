from sqlalchemy import Column, Integer, String
from library_app.database import Base

class Book(Base):
    __teblename__="books"

    id = Column(Integer, primary_key = True)
    title = Column(String, unique=True, nullable=False)
    author = Column(String, nullable=False)

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}')>"