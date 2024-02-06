#Stever Heinsaar 14.11.2023
#Turtle KT kujund 6

import turtle

#akna loomine
w = turtle.Screen()
w.setup(300,300)
w.title("S.Heinsaar Kujund 6")

kaugus = 100
kaugus2 = 40

#loome kilpkonna
def kujund():
    tommy = turtle.Turtle()
    tommy.speed("fastest")
    for i in range(4):
        tommy.fd(kaugus)
        tommy.lt(90)
        tommy.fd(kaugus2)
        tommy.lt(90)
        tommy.fd(kaugus)
        tommy.lt(90)
        tommy.fd(kaugus2)
        
        
kujund()




turtle.exitonclick()