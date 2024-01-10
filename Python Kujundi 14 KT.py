#Stever Heinsaar 14.11.2023
#Turtle KT kujund 14

import turtle


#akna loomine
w = turtle.Screen()
w.setup(300,300)
w.title("S.Heinsaar Kujund 14")

kaugus = 100

#loome kilpkonna
def kujund():
    johnny = turtle.Turtle()
    johnny.speed("fastest")
    for i in range(11):
        johnny.lt(8)
        for i in range(1):
            johnny.setpos(0,0)
            johnny.penup()
            johnny.fd(kaugus/2)
            johnny.lt(90)
            johnny.pendown()
            johnny.fd(kaugus/2)
            for j in range(3):
                johnny.lt(90)
                johnny.fd(kaugus)
            johnny.lt(90)
            johnny.fd(kaugus/2)
            johnny.penup()
        
        
        
kujund()


turtle.exitonclick()