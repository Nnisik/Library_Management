import tkinter
import sqlite3


conn = sqlite3.connect("library.db")
cur = conn.cursor()

def addNewUserToDB(login: str, password: str) -> None:
    cur.execute(
        """INSERT INTO users (login, password) VALUES (?, ?)""", 
        (login, password)
        )
    conn.commit()

def getAllUsersDataDict() -> dict:
    userDict={}
    for row in cur.execute("""SELECT * FROM users """):
        userDict['id'] =row[0]
        userDict['login']=row[1]
        userDict['password']=row[2]
    return userDict

def findUser(login: str) -> bool:
    for row in cur.execute("""SELECT * FROM users"""):
        if row[1]==login:
            return True
    return False

def getUserByLogin(login: str) -> list:
    if not findUser:
        print("User doesn't exist.")
    else:
        cur.execute(
            """SELECT * FROM users WHERE login=?""",
            (login)
            )
        return cur.fetchone()


# login class
class Login:
    def loginUser(self, login, password):
        self.login = login
        self.password = password

    # def checkUserExist(self):
    #     if db.checkUserExist(self.login):
    #         return True
    #     else:
    #         print("Login not exist")
    #         return False
    
    def getUserPassword(self):
        if self.checkUserExist():
            password = self.getUserPasswordByLogin(self.login)
            if password == self.password:
                # TODO: finnish authtentification
                pass

# signup class
class Signup:
    def signupUser(self, login, password, password_rpt):
        self.login = login
        self.password = password
        self.password_rpt = password_rpt

        if not self.checkUserNotExist():
            print('user with this name is alredy registered')
            exit()
        
        if self.passwordsMatch():
            print("Password and password repeat don't match")
            exit()
        
        # db.addNewUser(self)
    
    # def checkUserNotExist(self):
    #     if db.checkUserExist(self.login):
    #         print("This user already exists!")
    #         return False
    
    def passwordsMatch(self):
        return not self.password == self.password_rpt

class Book:
    def __init__(self, title: str, author: str, year:int, publisher:str, genre:str) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.genre = genre
    
    def printBookInfo(self) -> str:
        return f"{self.title} by {self.author}, {self.year}, {self.publisher}, {self.genre}"

# FIXME: connect to DB and rewrite to work with DB
class BookStorage:
    #TODO  
    def getAllBooks(self) -> None:
        pass
    
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
    
    def searchBookByTitle(self, title) -> list:
        books = []
        for book in self.bookList:
            if book.title == title:
                books.append(book)
        return books
    
    def searchBookByAuthor(self, author) -> list:
        books = []
        for book in self.bookList:
            if book.author == author:
                books.append(book)
        return books
    
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

class Root:
    def __init__(self, title: str) -> None:
        self.root = tkinter.Tk()
        self.root.title(title)

    def runApp(self) -> None:
        self.root.mainloop()

class SignUpGUI (Root):
    def __init__(self, title: str) -> None:
        super().__init__(title)

    # TODO: make it fancy

class LoginGUI (Root):
    def __init__(self, title: str) -> None:
        super().__init__(title)

        tkinter.Label(self.root, text=" " * 10).grid(row=0, column=0)
        tkinter.Label(self.root, text=" " * 20).grid(row=0, column=4)
        
        pageTitle = tkinter.Label(
            self.root, 
            text="Войти")
        pageTitle.grid(row=1, column=3)
        
        tkinter.Label(self.root, text=" " * 10).grid(row=2, column=0)

        tkinter.Label(self.root, text="Логин: ").grid(row=3, column=1)
        tkinter.Label(self.root, text="Пароль: ").grid(row=4, column=1)

        self.loginEntry = tkinter.Entry().grid(row=3, column=3)
        self.passwordEntry = tkinter.Entry().grid(row=4, column=3)

        tkinter.Label(self.root, text=" " * 10).grid(row=5, column=0)

        submitButton = tkinter.Button(
            self.root, 
            text="Продолжить", 
            command=self.__loginUser)
        submitButton.grid(row=6, column=3)

        tkinter.Label(self.root, text=" " * 10).grid(row=7, column=0)
        tkinter.Label(self.root, text=" " * 10).grid(row=8, column=0)

        signupButton = tkinter.Button(
            self.root, 
            text="Зарегестрироваться")
        signupButton.grid(row=9, column=3)

        tkinter.Label(self.root, text=" " * 10).grid(row=10, column=0)

    def __loginUser(self):
        login = self.loginEntry.get()
        password = self.passwordEntry.get()

        Login.loginUser(login, password)

class BookStorageGUI (Root):
    def __init__(self, title: str) -> None:
        super().__init__(title)

        tkinter.Label(self.root, text="Название: ").grid(row=0, column=0)
        tkinter.Label(self.root, text="Автор: ").grid(row=1, column=0)
        tkinter.Label(self.root, text="год: ").grid(row=2, column=0)
        tkinter.Label(self.root, text="Издательство: ").grid(row=3, column=0)
        tkinter.Label(self.root, text="Жанр: ").grid(row=4, column=0)

        self.titleEntry = tkinter.Entry(self.root).grid(row=0, column=1)
        self.authorEntry = tkinter.Entry(self.root).grid(row=1, column=1)
        self.yearEntry = tkinter.Entry(self.root).grid(row=2, column=1)
        self.publisherEntry = tkinter.Entry(self.root).grid(row=3, column=1)
        self.genreEntryl = tkinter.Entry(self.root).grid(row=4, column=1)

        tkinter.Label(self.root, text=" " * 10).grid(row=0, column=2)

        tkinter.Button(
            self.root, 
            text="Искать по Названию",
            command=self.__findBookByTitle).grid(row=0, column=3)
        
        tkinter.Button(
            self.root, 
            text="Искать по Автору",
            command=self.__findBookByAuthor).grid(row=1, column=3)
        
        tkinter.Button(
            self.root, 
            text="Искать по Году",
            command=self.__findBookByYear).grid(row=2, column=3)
        
        tkinter.Button(
            self.root, 
            text="Искать по Издателю",
            command=self.__findBookByPublish).grid(row=3, column=3)
        
        tkinter.Button(
            self.root, 
            text="Искать по Жанру",
            command=self.__findBookByGenre).grid(row=4, column=3)

        tkinter.Label(self.root, text=" " * 10).grid(row=0, column=4)

        addButton = tkinter.Button(
            self.root, 
            text="Добавить Книгу", 
            command=self.__addBook)
        addButton.grid(row=0, column=5)
        
        deleteButton = tkinter.Button(
            self.root, 
            text="Удалить Книгу", 
            command=self.__deleteBook)
        deleteButton.grid(row=1, column=5)

        tkinter.Label(self.root, text="").grid(row=5, column=0)

        self.bookList = tkinter.Listbox(self.root, width=50).grid(
            row=6, column=0, columnspan=3, padx=5, pady=5)

        tkinter.Label(self.root, text="    ").grid(row=0, column=6)

    def __clearListBox(self) -> None:
        self.bookList.delete(0, tkinter.END)

    # TODO: finish
    def __displayBooksInfo(self, books=None) -> None:
        self.__clearListBox()
        if books is None:
            # TODO: get information for all books from the DB
            bookList = BookStorage.getAllBooks()
            # TODO: for each of the book add it's data into a list box
            pass
        else:
            for book in books:
                self.bookList.insert(tkinter.END, book.printBookInfo())

    def __findBookByTitle(self) -> None:
        title = self.titleEntry.get()
        bookList = BookStorage.searchBookByTitle(title)
        self.displayBookInfo(bookList)

    def __findBookByAuthor(self) -> None:
        author = self.authorEntry.get()
        bookList = BookStorage.searchBookByAuthor(author)
        self.displayBookInfo(bookList)

    def __findBookByYear(self) -> None:
        year = self.yearEntry.get()
        bookList = BookStorage.searchBookByYear(year)
        self.displayBookInfo(bookList)

    def __findBookByPublish(self) -> None:
        publisher = self.publisherEntry.get()
        bookList = BookStorage.searchBookByPublisher(publisher)
        self.displayBookInfo(bookList)

    def __findBookByGenre(self) -> None:
        author = self.authorEntry.get()
        bookList = BookStorage.searchBookByAuthor(author)
        self.displayBookInfo(bookList)

    def __addBook(self) -> None:
        title = self.titleEntry.get()
        author = self.authorEntry.get()
        year = self.yearEntry.get()
        publisher = self.publisherEntry.get()
        genre = self.genreEntry.get()

        book = Book(title, author, year, publisher, genre)
        BookStorage.addBook(book)
        self.__displayBooksInfo()

    def __deleteBook(self) -> None:
        title = self.titleEntry.get()
        author = self.authorEntry.get()

        BookStorage.deleteBook(title, author)
        self.__displayBooksInfo()


if __name__ == "__main__":
    # app = LoginGUI("Book Storage App")
    # app.runApp()
    print(getAllUsersDataDict())