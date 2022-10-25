from tkinter import *
import math

win = Tk()
win.geometry("400x400")


def sum():
    x = int(a.get())
    y = int(b.get())
    sum1 = x + y
    label.config(text=sum1)


def riz():
    x = int(a.get())
    y = int(b.get())
    riz1 = x - y
    label.config(text=riz1)


def mno():
    x = int(a.get())
    y = int(b.get())
    mno1 = x * y
    label.config(text=mno1)


def dil():
    x = int(a.get())
    y = int(b.get())
    dil1 = x / y
    label.config(text=dil1)


def zve():
    x = int(a.get())
    y = int(b.get())
    zve1 = x ** y
    label.config(text=zve1)


def k2k():
    x = int(a.get())
    k2k1 = math.sqrt(x)
    label.config(text=k2k1)


def k3k():
    x = int(a.get())
    k3k1 = x ** (1 / 3)
    label.config(text=k3k1)


Label(win, text="Введіть перше число ", font=('Calibri 17')).pack()
a = Entry(win, width=35)
a.pack()
Label(win, text="Введіть друге число ", font=('Calibri 17')).pack()
b = Entry(win, width=35)
b.pack()

label = Label(win, text="Результат ", font=('Calibri 17'))
label.pack(pady=20)

Button(win, text="Додавання чисел", command=sum,bg="sky blue").pack()
Button(win, text="Віднімання чисел", command=riz,bg="sky blue").pack()
Button(win, text="Множення чисел", command=mno,bg="sky blue").pack()
Button(win, text="Ділення числа", command=dil,bg="sky blue").pack()
Button(win, text="Зведення числа в ступінь", command=zve,bg="sky blue").pack()
Button(win, text="Квадратний корінь першого числа", command=k2k,bg="sky blue").pack()
Button(win, text="Кубічний корінь першого числа", command=k3k,bg="sky blue").pack()

win.mainloop()