#Stever Heinsaar 9.11.2023
#Ülesanne 2 Turtle

import turtle

#akna loomine
w = turtle.Screen()
w.setup(300,300)
w.title("S.Heinsaar Ülesanne 02")

kaugus = 100
nurk = 144
nurkadearv = 5
kolmnurk = 3
kolmnurknurk = 120

#loome kilpkonna
def viisnurk():
    john = turtle.Turtle()
    for i in range (nurkadearv):
        #print(i)
        john.fd(kaugus)
        john.rt(nurk)

def kolmnurk(n, k, kn):
    john2 = turtle.Turtle()
    john2.color("red")
    for j in range(n):
        john2.fd(-k)
        john2.rt(kn)
        
kolmnurk(3, 100, 120)


turtle.exitonclick()