from tkinter import *
from tkinter import ttk


class Main(object):
    def __init__(self, master):
        self.master = master

        # frames
        mainFrame = Frame(self.master)
        mainFrame.pack()

        #top frames
        topFrame = Frame(mainFrame, width=1350, height=70, bg="#fafafa", padx=20, relief=SUNKEN, borderwidth=2)
        topFrame.pack(side=TOP, fill=X)

        #center frame
        centerFrame = Frame( mainFrame, width=1350, relief=RIDGE, bg='#e0f0f0', height=680)
        centerFrame.pack(side=TOP)

        #Center left Frame
        centerLeftFrame = Frame(centerFrame, width=900, height=700, bg='#e0f0f0', borderwidth=2, relief='sunken')
        centerLeftFrame.pack(side=LEFT)

        # center right frame
        centerRightFrame = Frame(centerFrame,  width=450, height=700, bg='#e0f0f0', borderwidth=2, relief='sunken')
        centerRightFrame.pack()

        #search bar
        search_bar = LabelFrame(centerRightFrame, width=440, height=75, text="Search Box", bg="#9bc977")
        search_bar.pack(fill=BOTH)

        #list bar
        list_bar = LabelFrame(centerRightFrame, width=440, height=175, text='List Box', bg='#fcc324')
        list_bar.pack(fill=BOTH)

        #add book
        self.btnbook = Button(topFrame, text='Add Book', font='arial 12 bold')
        self.btnbook.pack(side=LEFT,padx=10)

        #add member button
        self.btnmembers=Button(topFrame, text='Add Member', font='arial 12 bold', padx=10)
        self.btnmembers.pack(side=LEFT)

        #give book
        self.btngive=Button(topFrame, text='Give Book', font='arial 12 bold', padx=10)
        self.btngive.pack(side=LEFT)



def main():
    root = Tk()
    app = Main(root)
    root.title("Library Management System")
    root.geometry("1350x750+350+200")
    # root.iconitmap("icons/book.png")
    root.mainloop()


if __name__=="__main__":
    main()