import tkinter
from tkinter import *
import back

def get_selected_row(event):
    global selected_row
    index = list.curselection()[0]
    selected_row = list.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_row[1])
    e2.delete(0,END)
    e2.insert(END,selected_row[2])
    e3.delete(0,END)
    e3.insert(END,selected_row[3])
    e4.delete(0,END)
    e4.insert(END,selected_row[4])
    e5.delete(0,END)
    e5.insert(END,selected_row[5])
    e6.delete(0,END)
    e6.insert(END,selected_row[6])

def delete_command():
    back.delete(selected_row[0])

def view_command():
    list.delete(0,END)
    for rows in back.view():
        list.insert(END,rows)

def search_command():
    list.delete(0,END)
    for rows in back.search(Date_text.get(), Earnings_text.get(), Excercise_text.get(), Study_text.get(), Diet_text.get(), Python_text.get()):
        list.insert(END,rows)

def add_command():
    back.insert(Date_text.get(), Earnings_text.get(), Excercise_text.get(), Study_text.get(), Diet_text.get(), Python_text.get())

    list.delete(0,END)
    list.insert(END, (Date_text.get(), Earnings_text.get(), Excercise_text.get(), Study_text.get(), Diet_text.get(), Python_text.get()))

win = Tk()

win.wm_title('MY ROUTINE DATABASE')

l1 = Label(win, text='Date')
l1.grid(row=0,column=0)
l2 = Label(win, text='Earnings')
l2.grid(row=0,column=2)
l3 = Label(win, text='Excercise')
l3.grid(row=1,column=0)
l4 = Label(win, text='Study')
l4.grid(row=1,column=2)
l5 = Label(win, text='Diet')
l5.grid(row=2,column=0)
l6 = Label(win, text='Python')
l6.grid(row=2,column=2)

Date_text = StringVar()
e1 = Entry(win, textvariable=Date_text)
e1.grid(row=0,column=1)

Earnings_text = StringVar()
e2 = Entry(win, textvariable=Earnings_text)
e2.grid(row=0,column=3)

Excercise_text = StringVar()
e3 = Entry(win, textvariable=Excercise_text)
e3.grid(row=1,column=1)

Study_text = StringVar()
e4 = Entry(win, textvariable=Study_text)
e4.grid(row=1,column=3)

Diet_text = StringVar()
e5 = Entry(win, textvariable=Diet_text)
e5.grid(row=2,column=1)

Python_text = StringVar()
e6 = Entry(win, textvariable=Python_text)
e6.grid(row=2,column=3)

list = Listbox(win, height=8, width=35)
list.grid(row=3,column=0,rowspan=9,columnspan=2)

sb = Scrollbar(win)
sb.grid(row=3,column=2,rowspan=9)

list.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(win, text='ADD', width=12, pady=5, command=add_command)
b1.grid(row=3,column=3)
b2 = Button(win, text='Search', width=12, pady=5, command=search_command)
b2.grid(row=4,column=3)
b3 = Button(win, text='Delete Date', width=12, pady=5, command=delete_command)
b3.grid(row=5,column=3)
b4 = Button(win, text='View All', width=12, pady=5, command=view_command)
b4.grid(row=6,column=3)
b5 = Button(win, text='Close', width=12, pady=5, command=win.destroy)
b5.grid(row=7,column=3)

win.mainloop()
