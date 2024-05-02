from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base
from models.book import Book
from models.author import Author

engine = create_engine('sqlite:///library.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

author1 = Author(first_name='Тарас', last_name='Шевченко')
book1 = Book(title='Кобзар', year=1840, isbn='1234567890', author=author1)
author1.books.append(book1)
book2 = Book(title='Заповіт', year=1845, isbn='9789669470687', author=author1)
author1.books.append(book2)
session.add(author1)

author2 = Author(first_name='Леся', last_name='Українка')
book3 = Book(title='Лірика', year=1893, isbn='9789669462187', author=author2)
author2.books.append(book3)
book4 = Book(title='Лісова Пісня', year=1911, isbn='9789669462194', author=author2)
author2.books.append(book4)
session.add(author2)

author3 = Author(first_name='Михайло', last_name='коцюбинський')
book5 = Book(title='Intermezzo', year=1889, isbn='9789669462262', author=author3)
author3.books.append(book5)
book6 = Book(title='Тіні забутих предків', year=1911, isbn='9789669462255', author=author3)
author3.books.append(book6)
session.add(author3)

author4 = Author(first_name='Іван', last_name='Франко')
book7 = Book(title='Мойсей', year=1889, isbn='9789661461883', author=author4)
author4.books.append(book7)
book8 = Book(title='Лісова пісня', year=1906, isbn='9789661461845', author=author4)
author4.books.append(book8)
session.add(author4)

author5 = Author(first_name='Ольга', last_name='Кобилянська')
book9 = Book(title='Записки сумнівного', year=1896, isbn='9789661826817', author=author5)
author5.books.append(book9)
session.add(author5)

author6 = Author(first_name='Марко', last_name='Вовчок')
book10 = Book(title='Слово про Україну', year=1887, isbn='9789661827418', author=author6)
author6.books.append(book10)
book11 = Book(title='Богатирська старина', year=1892, isbn='9789661827449', author=author6)
author6.books.append(book11)
session.add(author6)

author7 = Author(first_name='Іван', last_name='Липа')
book12 = Book(title='Козацькі легенди', year=1930, isbn='9789677827449', author=author7)
author7.books.append(book12)
session.add(author7)

author8 = Author(first_name='Василь', last_name='Стус')
book13 = Book(title='Струни забуття', year=1957, isbn='1234567897', author=author8)
author8.books.append(book13)
session.add(author8)

author9 = Author(first_name='Іван', last_name='Багряний')
book14 = Book(title='Маруся Чурай', year=1928, isbn='1234567898', author=author9)
author9.books.append(book14)
session.add(author9)

session.commit()

authors = session.query(Author).all()
for author in authors:
    print(f"Author: {author.first_name} {author.last_name}")
    for book in author.books:
        print(f"Book: {book.title}, Year: {book.year}, ISBN: {book.isbn}")


users = session.query(Author).all()