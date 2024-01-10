#Stever Heinsaar
#28.11.2023
#Hinne: Kilpkonn (IF, FOR)
import turtle
import random

"""
- funktsioon, mis loob erineva suuruse ja asukohaga viisnurga kogu platsi ulatuses (üle ääre ei tohi minna)
- funktsioon, mis loob erineva suuruse ja asukohaga kolmnurki kogu platsi ulatuses
- funktsioon, mis kasutab eelmisi funktsioone, et luua suvaliselt viisnurki ja kolmnurki
- menüü -> küsib kasutajalt, millist kujundit soovib, küsib kogust ja kui ära joonistab, siis küsib jälle. EXIT võimalus.
"""
w = turtle.Screen()
w.setup(600,600)

def viisnurk():
    a = random.randint(50,200)
    x = random.randint(-300,300-a)
    y = random.randint(-300+(a//1.15),300-(a//1.18))
    tommy = turtle.Turtle()
    tommy.hideturtle()
    tommy.speed("fastest")
    tommy.penup()
    tommy.goto(x,y)
    tommy.pendown()
    tommy.left(random.randint(0,360))
    for i in range(5):
        tommy.fd(a)
        tommy.rt(144)

def kolmnurk():
    a = random.randint(50,200)
    x = random.randint(-300,300-a)
    y = random.randint(-300+(a//2),300-(a//2))
    tommy = turtle.Turtle()
    tommy.hideturtle()
    tommy.speed("fastest")
    tommy.penup()
    tommy.goto(x,y)
    tommy.pendown()
    for j in range(3):
        tommy.fd(a)
        tommy.rt(120)
        

def suvaline():
    suv = random.randint(1,2)
    print(suv)
    if suv == 1:
        viisnurk()
    else:
        kolmnurk()

def menuu():
    loop = 1
    while loop==1:
        vali_kujund = w.numinput("Kujundi valik","1. Vali viisnurk \n2. Vali kolnurk \n3. Vali suvaline \n4. EXIT")
        if vali_kujund >= 4:
            exit()
        vali_kogus = int(w.numinput("Kujundite arv","Vali kujundite arv: "))
        for i in range(vali_kogus):
            if vali_kujund == 1:
                viisnurk()
            elif vali_kujund == 2:
                kolmnurk()
            elif vali_kujund == 3:
                suvaline()
            else:
                print("EXIT")

menuu()    

turtle.exitonclick()