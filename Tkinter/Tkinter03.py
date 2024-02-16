#Stever Heinsaar
#16.02.2024
from tkinter import *
from tkinter import ttk

#aken
aken = Tk()
aken.title("Käibemaksukalkulaator")
aken.geometry("250x150")

#rida 1
tekst1 = Label(aken, text="Hind Käibemaksuta:")
tekst1.grid(row=0, column=0)

hind = Entry(aken)
hind.grid(row=0, column=1)

#rida 2
tekst2 = Label(aken, text="Käibemaksumäär:")
tekst2.grid(row=1, column=0)

var = IntVar()
valikukast = Radiobutton(aken, text="9%", variable=var, value=9)
valikukast.grid(row=1, column=1)
valikukast = Radiobutton(aken, text="22%", variable=var, value=22)
valikukast.grid(row=2, column=1)

# 22% vaikimisi valitud
var.set(22)

#joon
joon = ttk.Separator(aken, orient=HORIZONTAL)
joon.grid(row=3, column=0, columnspan=2, sticky="ew")

#rida 3
tekst3 = Label(aken, text="Käibemaks:")
tekst3.grid(row=4, column=0)

valjund1 = Label(aken, text="0.00€")
valjund1.grid(row=4, column=1)

#rida 4
tekst4 = Label(aken, text="Hind Käibemaksuga:")
tekst4.grid(row=5, column=0)

valjund2 = Label(aken, text="0.00€")
valjund2.grid(row=5, column=1)

#nupp
nupp = Button(aken, text="Arvuta", command=lambda: arvuta())
nupp.grid(row=6, column=0, columnspan=2)

#funktsioon
def arvuta():
    hind_käibemaksuta = float(hind.get())
    käibemaksumäär = 9 if var.get() == 9 else 22
    käibemaks = hind_käibemaksuta * käibemaksumäär / 100
    hind_käibemaksuga = hind_käibemaksuta + käibemaks
    valjund1.config(text=str(käibemaks) + "€")
    valjund2.config(text=str(hind_käibemaksuga) + "€")

aken.mainloop()