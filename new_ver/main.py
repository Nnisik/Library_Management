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
        self.lbl_search=Label(search_bar, text="Search :", font='ariel 12 bold', bg='#9bc977', fg='white')
        self.lbl_search.grid(row=0,column=0,padx=20, pady=10)
        self.ent_search=Entry(search_bar, width=30, bd=10)
        self.ent_search.grid(row=0,column=1,columnspan=3,pady=10)
        self.btn_search=Button(search_bar,text='Search',font='ariel 12',bg='#fcc324',fg='white')
        self.btn_search.grid(row=0,column=4,padx=20,pady=10)

        #list bar
        list_bar = LabelFrame(centerRightFrame, width=440, height=175, text='List Box', bg='#fcc324')
        list_bar.pack(fill=BOTH)
        lbl_list=Label(list_bar,text='Short By',font='times 16 bold',fg='#2488ff',bg='#fcc324')
        lbl_list.grid(row=0,column=2)
        self.listChoise=IntVar()
        rb1=Radiobutton(list_bar,text='All Books',var=self.listChoise,value=1,bg='#fcc324')
        rb2=Radiobutton(list_bar,text='In Library',var=self.listChoise,value=2,bg='#fcc324')
        rb3=Radiobutton(list_bar,text='Borrowed Books',var=self.listChoise,value=3,bg='#fcc324')
        rb1.grid(row=1,column=0)
        rb2.grid(row=1,column=1)
        rb3.grid(row=1,column=2)
        btn_list=Button(list_bar, text="List Books",bg='#2488ff',fg='white',font='ariel 12')
        btn_list.grid(row=1,column=3,padx=40,pady=10)

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