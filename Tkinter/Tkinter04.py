#Stever Heinsaar
#16.02.2024
from tkinter import *
from PIL import ImageTk, Image

#aken
aken = Tk()
aken.title("Botswana Lipp")

#lipp
lipp = Canvas(aken, width=1350, height=500)
lipp.pack()

# Draw the flag
lipp.create_rectangle(0, 0, 500, 150, fill="steelblue2")
lipp.create_rectangle(0, 150, 500, 175, fill="white")
lipp.create_rectangle(0, 175, 500, 225, fill="black")
lipp.create_rectangle(0, 225, 500, 250, fill="white")
lipp.create_rectangle(0, 250, 500, 400, fill="steelblue2")


#pilt
minu_pilt = ImageTk.PhotoImage(Image.open("zebra.png"))
lipp.create_image(410, 0, anchor=NW, image=minu_pilt)



aken.mainloop()