import db

class Book:
    def __init__(self, title: str, author: str, year:int, publisher:str, genre:str) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.genre = genre
    
    def printBookInfo(self) -> None:
        print(f"{self.title} by {self.author}, {self.year}, {self.publisher}, {self.genre}")

# FIXME: connect to DB and rewrite to work with DB
class BookStorage: 
    def __init__(self) -> None:
        self.bookList = []
    
    def addBook(self, book: Book) -> None:
        if book not in self.bookList:
            self.bookList.append(book)
        else:
            print("This book is already in a library.")
    
    def deleteBook(self, title, author) -> None:
        for book in self.bookList:
            if book.title == title and book.author == author:
                self.bookList.remove(book)
                return
        print(f'No book "{title}" by {author} found.')
    
    def displayBooks(self) -> None: 
        for book in self.bookList:
            book.printBookInfo()
    
    def searchBookByTitle(self, title) -> Book:
        for book in self.bookList:
            if book.title == title:
                return book
    
    def searchBookByAuthor(self, author) -> list:
        for book in self.bookList:
            if book.author == author:
                return book
    
    def searchBookByYear(self, year) -> list:
        books = []
        for book in self.bookList:
            if book.year == year:
                books.append(book)
        return books
    
    def searchBookByPublisher(self, publisher) -> list:
        books = []
        for book in self.bookList:
            if book.publisher == publisher:
                books.append(book)
        return books

    def searchBookByGenre(self, genre) -> list:
        books = []
        for book in self.bookList:
            if book.genre == genre:
                books.append(book)
        return books
