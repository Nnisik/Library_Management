import sqlite3
from bookClasses import Book


# connection to database
def cursor():
    return sqlite3.connect("projectDB.py").cursor()


# user commands 
def createNewUser(login: str, password: str) -> None:
    c = cursor()
    with c.connection:
        c.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login, password))


# book commands
def getBooks() -> list:
    c = cursor()
    booksList=[]
    with c.connection:
        c.execute("SELECT * FROM books")
        print(c.fetchall())

def addNewBook(book: Book, id) -> None:
    c = cursor()
    with c.connection:
        # insert new book
        c.execute("INSERT INTO books (title, author, year, publisher, genre) VALUES (?, ?, ?, ?, ?)", (book.title, book.author, book.year, book.publisher, book.genre))
