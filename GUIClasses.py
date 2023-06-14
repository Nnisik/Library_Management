import tkinter
from bookClasses import Book, BookStorage


class Root:
    def __init__(self, title: str) -> None:
        self.root = tkinter.Tk()
        # self.root.config('')
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

    # TODO: make it beautiful


class BookStorageGUI (Root):
    def __init__(self, title: str) -> None:
        super().__init__(title)

        titleLabel = tkinter.Label(self.root, text="Title: ").grid(row=0, column=0)
        authorLabel = tkinter.Label(self.root, text="Author: ").grid(row=1, column=0)
        yearLabel = tkinter.Label(self.root, text="Year: ").grid(row=2, column=0)
        publishLabel = tkinter.Label(self.root, text="Publisher: ").grid(row=3, column=0)
        genreLabel = tkinter.Label(self.root, text="Genre: ").grid(row=4, column=0)

        self.titleEntry = tkinter.Entry(self.root).grid(row=0, column=1)
        self.authorEntry = tkinter.Entry(self.root).grid(row=1, column=1)
        self.yearEntry = tkinter.Entry(self.root).grid(row=2, column=1)
        self.publisherEntry = tkinter.Entry(self.root).grid(row=3, column=1)
        self.genreEntryl = tkinter.Entry(self.root).grid(row=4, column=1)

        tkinter.Label(self.root, text="          ").grid(row=0, column=2)

        titleSearchButton = tkinter.Button(self.root, text="Search by Title", command=self.__findBookByTitle).grid(row=0, column=3)
        titleSearchButton = tkinter.Button(self.root, text="Search by Author", command=self.__findBookByAuthor).grid(row=1, column=3)
        titleSearchButton = tkinter.Button(self.root, text="Search by Year", command=self.__findBookByYear).grid(row=2, column=3)
        titleSearchButton = tkinter.Button(self.root, text="Search by Publisher", command=self.__findBookByPublish).grid(row=3, column=3)
        titleSearchButton = tkinter.Button(self.root, text="Search by Genre", command=self.__findBookByGenre).grid(row=4, column=3)

        tkinter.Label(self.root, text="          ").grid(row=0, column=4)

        addButton = tkinter.Button(self.root, text="Add Book", command=self.__addBook).grid(row=0, column=5)
        deleteButton = tkinter.Button(self.root, text="Delete Book", command=self.__deleteBook).grid(row=1, column=5)
        
        tkinter.Label(self.root, text="").grid(row=5, column=0)

        self.bookList = tkinter.Listbox(self.root, width=50).grid(row=6, column=0, columnspan=3, padx=5, pady=5)

    
    # TODO:
    def __clearListBox(self) -> None:
        pass
    
    # TODO:
    def __displayBooksInfo(self, books=None) -> None:
        self.__clearListBox()
        if books is None:
            pass
        else:
            pass
    
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
    
    # TODO
    def __deleteBook(self) -> None:
        pass

