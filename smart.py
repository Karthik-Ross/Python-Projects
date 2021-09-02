import tkinter
from tkinter import *

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def div(a,b):
    return a / b

def mul(a,b):
    return a * b

def mod(a,b):
    return a % b

def lcm(a,b):
    L = a if a > b else b
    while L <= a * b:
        if L%a == 0 and L%b == 0:
            return L
        L += 1

def hcf(a,b):
    H = a if a < b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H -= 1

def extract_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract_from_text(text)
                r = operations[word.upper()](l[0], l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'Something went wrong please enter the word correctly')
            finally:
                break
        elif word.upper() in operations.keys():
            list.delete(0,END)
            list.insert(END,'Something went wrong please enter the word correctly')


operations = {'ADD':add, 'ADDITION':add, 'PLUS':add, 'SUM':add,
              'SUB':sub, 'SUBTRACTION':sub, 'MINUS':sub, 'DIFFERENCE':sub,
              'MULTIPLY':mul, 'PRODUCT':mul, 'MULTIPLICATION':mul, 'MULTIPLIED':mul,
              'DIVISION':div, 'DIV':div, 'DIVIDED':div, 'DIVIDE':div, 'LCM':lcm, 'HCF':hcf,
              'REMAINDER':mod, 'MODULUS':mod, 'MOD':mod}

win = Tk()
win.title('Smart Calculator')
win.geometry('500x300')
win.configure(bg='lightskyblue')

l1 = Label(win, text='I am a smart calculator', width=25, padx=3)
l1.place(x=150, y=10)
l2 = Label(win, text='My name is Pugger', padx=3)
l2.place(x=185, y=40)
l3 = Label(win, text='What can I help you', padx=3)
l3.place(x=185, y=130)

textin = StringVar()
e1 = Entry(win, width=30, textvariable=textin)
e1.place(x=150, y=163)
b1 = Button(win, text='Calculate', command=calculate)
b1.place(x=210, y=192)
list = Listbox(win, width=25,height=3,bd=2)
list.place(x=165,y=230)

win.mainloop()
