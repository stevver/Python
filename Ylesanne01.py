#Stever Heinsaar 9.11.2023
#Ülesanne 1 Turtle

import turtle

#akna loomine
w = turtle.Screen()
w.setup(300,300)
w.title("S.Heinsaar Ülesanne 01")

turtle.speed("fastest")

kaugus = 100

#loome kilpkonna
john = turtle.Turtle()
john.color("lime")
john.fd(kaugus)

tom = turtle.Turtle()
tom.color("red")
tom.lt(45)
tom.fd(kaugus)

tom2 = turtle.Turtle()
tom2.color("orange")
tom2.lt(90)
tom2.fd(kaugus)

tom3 = turtle.Turtle()
tom3.color("blue")
tom3.lt(135)
tom3.fd(kaugus)

tom3 = turtle.Turtle()
tom3.color("blue")
tom3.rt(180)
tom3.fd(kaugus)

john = turtle.Turtle()
john.color("lime")
john.rt(145)
john.bk(kaugus)

tom = turtle.Turtle()
tom.color("red")
tom.rt(270)
tom.bk(kaugus)

tom2 = turtle.Turtle()
tom2.color("orange")
tom2.rt(360)
tom2.bk(kaugus)



turtle.exitonclick()