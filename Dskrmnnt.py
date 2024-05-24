import matplotlib.pyplot as plt
import numpy as np
import math
from tkinter import *

def diskriminant():
    a = float(texbox1.get())
    b = float(texbox2.get())
    c = float(texbox3.get())

    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = round((-b + math.sqrt(D)) / (2 * a), 2)
        x2 = round((-b - math.sqrt(D)) / (2 * a), 2)
        vastus.configure(text=f"x1 = {x1}, x2 = {x2}")
        grafik(a, b, c)
    elif D == 0:
        x1 = round(-b / (2 * a), 2)
        vastus.configure(text=f"x = {x1}")
        grafik(a, b, c)
    else:
        vastus.configure(text="ei saa laheda")

def grafik(a, b, c):
    x0 = -b / (2 * a)
    y0 = a * x0 ** 2 + b * x0 + c
    x_values = np.arange(x0 - 10, x0 + 10, 0.5)
    y_values = a * x_values ** 2 + b * x_values + c

    plt.figure()
    plt.plot(x_values, y_values, 'r-')
    plt.title('Ruutvõrrandi graafik')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

def rohkem():
    f.grid(row=4, column=0, columnspan=7)
    kala.grid(row=0, column=0)
    konn.grid(row=2, column=0)

def kalaGR():

    x1=np.arange(0,9.5,0.5)
    y1=(2/27)*x1**2-3
    x2=np.arange(-10,0.5,0.5)
    y2=0.04*x2**2-3
    x3=np.arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3,9.5,0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=np.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5,7.95,0.05)
    y6=(1/8)*(x6-7)**2+1.5
    x7=np.arange(-13,-8.5,0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8=np.arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15,-9.5,0.5)
    y9=[1]*len(x9)
    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)
    whaleGraph=plt.figure()
    for i in range(10):
        plt.plot(locals()[f'x{i+1}'],locals()[f'y{i+1}'])
    plt.title('Vaal')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()


def liblikasGR():
    x1=np.arange(-9,-1,0.5)
    y1=(-1/8)*(x1+9)**2+8
    x2=np.arange(1,9,0.5)
    y2=(-1/8)*(x2-9)**2+8
    x3=np.arange(-9,-8,0.5)
    y3=7*(x3+8)**2+1
    x4=np.arange(8,9,0.5)
    y4=7*(x4-8)**2+1
    x5=np.arange(-8,-1,0.5)
    y5=(1/49)*(x5+1)**2
    x6=np.arange(1,8,0.5)
    y6=(1/49)*(x6-1)**2
    x7=np.arange(-8,-1,0.5)
    y7=(-4/49)*(x7+1)**2
    x8=np.arange(1,8,0.5)
    y8=(-4/49)*(x8-1)**2
    x9=np.arange(-8,-2,0.5)
    y9=(1/3)*(x9+5)**2-7
    x10=np.arange(2,8,0.5)
    y10=(1/3)*(x10-5)**2-7
    x11=np.arange(-2,-1,0.5)
    y11=(-2)*(x11+1)**2-2
    x12=np.arange(1,2,0.5)
    y12=(-2)*(x12-1)**2-2
    x13=np.arange(-1,1,0.5)
    y13=(-1)*(4*x13**2)+2
    x14=np.arange(-1,1,0.5)
    y14=4*x14**2-6
    x15=np.arange(-2,0,0.5)
    y15=(-1)*(1.5*x15)+2
    x16=np.arange(0,2,0.5)
    y16=1.5*x16+2
    butterflyGraph=plt.figure()
    for i in range(16):
        plt.plot(locals()[f'x{i+1}'],locals()[f'y{i+1}'])
    plt.title('Liblikas')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

aken = Tk()
aken.geometry("800x600")
aken.title("Võrrandi lahendamine")

pealkiri = Label(aken,
                 text="Võrrandi lahendamine",
                 bg="#a3c9f7",
                 fg="#94041f",
                 font="Algerian 20",
                 height=3)
texbox1 = Entry(aken,
                bg="#a3c9f7",
                fg="#94041f",
                font="Algerian 20",
                width=5)
EText = Label(aken,
              text="x^2 +",
              bg="#a3c9f7",
              fg="#94041f",
              font="Algerian 20")
texbox2 = Entry(aken,
                bg="#a3c9f7",
                fg="#94041f",
                font="Algerian 20",
                width=5)
TText = Label(aken, text="x +",
              bg="#a3c9f7",
              fg="#94041f",
              font="Algerian 20")
texbox3 = Entry(aken,
                bg="#a3c9f7",
                fg="#94041f",
                font="Algerian 20",
                width=5)
KText = Label(aken, text=" = 0",
              bg="#a3c9f7",
              fg="#94041f",
              font="Algerian 20")
NuppLahenda = Button(aken,
                     bg="#a3c9f7",
                     fg="#94041f",
                     text="lahenda",
                     font="Algerian 15",
                     height=3, width=10,
                     relief=RAISED,
                     command=diskriminant)
vastus = Label(aken,
               bg="#a3c9f7",
               fg="#94041f",
               font="Algerian 20",
               justify=CENTER, height=3)
NuppRohkem = Button(aken,
                    bg="#a3c9f7",
                    fg="#94041f",
                    text="rohkem",
                    font="Algerian 15",
                    height=3, width=10,
                    relief=RAISED,
                    command=rohkem)
f = Frame(aken)
var = IntVar()
kala = Radiobutton(f,
                   text="kala",
                   variable=var,
                   value=1,
                   command=kalaGR)

konn = Radiobutton(f,
                   text="liblikas",
                   variable=var,
                   value=3,
                   command = liblikasGR)

pealkiri.grid(row=0, column=0, columnspan=7)
texbox1.grid(row=1, column=0)
EText.grid(row=1, column=1)
texbox2.grid(row=1, column=2)
TText.grid(row=1, column=3)
texbox3.grid(row=1, column=4)
KText.grid(row=1, column=5)
NuppLahenda.grid(row=1, column=6)
vastus.grid(row=2, column=0, columnspan=7)
NuppRohkem.grid(row=3, column=0, columnspan=7)

aken.mainloop()
