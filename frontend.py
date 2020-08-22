"""
This program can store the following information:
Title, Autor, Year, ISBN

The user is able to:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
from backend import Database

database=Database()

w_ = Tk()

w_.wm_title("Book Store")


def get_selected_row_(event):
    global selected_tuple_
    try:
        index=listbox_.curselection()[0]
        selected_tuple_= listbox_.get(index)
        entry_1.delete(0,END)
        entry_1.insert(END, selected_tuple_[1])
        entry_2.delete(0,END)
        entry_2.insert(END, selected_tuple_[2])
        entry_3.delete(0,END)
        entry_3.insert(END, selected_tuple_[3])
        entry_4.delete(0,END)
        entry_4.insert(END, selected_tuple_[4])
    except IndexError:
        pass


def view_all_():
    listbox_.delete(0,END)
    for row in database.view():
        listbox_.insert(END, row)

def search_():
    listbox_.delete(0, END)
    title=keeper_1.get()
    author=keeper_2.get()
    year=keeper_3.get()
    isbn=keeper_4.get()
    results = database.search(title, author, year, isbn)
    for row in results:
        listbox_.insert(END, row)
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    entry_3.delete(0,END)
    entry_4.delete(0,END)

def add_():
    title=keeper_1.get()
    author=keeper_2.get()
    year=keeper_3.get()
    isbn=keeper_4.get()
    database.insert(title, author, year, isbn)
    listbox_.delete(0,END)
    listbox_.insert(END, (title, author, year, isbn))
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    entry_3.delete(0,END)
    entry_4.delete(0,END)

def update_():
    title=keeper_1.get()
    author=keeper_2.get()
    year=keeper_3.get()
    isbn=keeper_4.get()
    id = int(selected_tuple_[0])
    database.update(id, title, author, year, isbn)
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    entry_3.delete(0,END)
    entry_4.delete(0,END)
    view_all_()

def delete_():
    database.delete(selected_tuple_[0])
    view_all_()
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    entry_3.delete(0,END)
    entry_4.delete(0,END)

label_1 = Label(w_, text="Title")
label_2 = Label(w_, text="Autor")
label_3 = Label(w_, text="Year")
label_4 = Label(w_, text="ISBN")

keeper_1 = StringVar()
keeper_2 = StringVar()
keeper_3 = StringVar()
keeper_4 = StringVar()

entry_1 = Entry(w_, textvariable=keeper_1)
entry_2 = Entry(w_, textvariable=keeper_2)
entry_3 = Entry(w_, textvariable=keeper_3)
entry_4 = Entry(w_, textvariable=keeper_4)

label_1.grid(row=0, column=0)
entry_1.grid(row=0, column=1)
label_2.grid(row=0, column=2)
entry_2.grid(row=0, column=3)
label_3.grid(row=1, column=0)
entry_3.grid(row=1, column=1)
label_4.grid(row=1, column=2)
entry_4.grid(row=1, column=3)


button_1=Button(w_, text="View all", width=12, command=view_all_)
button_1.grid(row=2, column=3)
button_2=Button(w_, text="Search entry", width=12, command=search_)
button_2.grid(row=3, column=3)
button_3=Button(w_, text="Add entry" ,width=12, command=add_)
button_3.grid(row=4, column=3)
button_4=Button(w_, text="Update", width=12, command=update_)
button_4.grid(row=5, column=3)
button_5=Button(w_, text="Delete", width=12, command=delete_)
button_5.grid(row=6, column=3)
button_6=Button(w_, text="Close" ,width=12, command = w_.destroy)
button_6.grid(row=7, column=3)

listbox_ = Listbox(w_, height=6, width=35)
listbox_.grid(row=2, column=0, rowspan=6, columnspan=2)
listbox_.bind("<<ListboxSelect>>", get_selected_row_)


scroll_=Scrollbar(w_)
scroll_.grid(row=2, rowspan=8, column=2)

listbox_.configure(yscrollcommand=scroll_.set)
scroll_.configure(command=listbox_.yview)

mainloop()
