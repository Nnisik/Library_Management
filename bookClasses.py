class Book:
    def __init__(self, title: str, author: str, year:int, publisher:str, genre:str) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.genre = genre
    
    def printBookInfo(self) -> None:
        print(f"{self.title} by {self.author}, {self.year}, {self.publisher}, {self.genre}")

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