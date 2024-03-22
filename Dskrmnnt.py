
from tkinter import *
aken = Tk()
aken.geometry("800x600")
tekst =  "Решение квадратного уровнения\n"
pealkiri = Label(aken,
                 text = tekst,
                 bg = "#a3c9f7",
                 fg = "#94041f",
                 font = "Algerian 20",
                 height = 3, width= len(tekst))
                 
texbox1 = Entry(aken,
                bg = "#a3c9f7",
                fg = "#94041f",
                font = "Algerian 20",
                width = 5)
EText = Label(aken,
                 text ="x**2",
                 bg = "#a3c9f7",
                 fg = "#94041f",
                 font = "Algerian 20")
texbox2 = Entry(aken,
                bg = "#a3c9f7",
                fg = "#94041f",
                font = "Algerian 20",
                width = 5)

pealkiri.pack()

texbox1.pack(side = LEFT)
EText.pack(side = LEFT)
texbox2.pack(side = LEFT)
aken.mainloop()
