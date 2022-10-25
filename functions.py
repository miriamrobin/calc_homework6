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

