#Stever Heinsaar
#14.11.2023
#Ülesanne 02

from math import *
import turtle
"""
Kilpkonn - küsib kasutajalt mingi raadisut
           kasutab funktsiooni ringi joonistamiseks
"""
w = turtle.Screen()

def ring(r):
    tommy = turtle.Turtle()
    tommy.circle(r)
raadius = w.numinput("Ringi loomine","Sisesta ringi raadius:")

ring(raadius)
turtle.exitonclick()

"""
Kütusekulu arvutamine
    Kasutaja sisestab tangitud kütuse liitrid
    Kasutaja sisestab läbitud kilomeetrid
    Programm leiab kütusekulu 100km kohta keskmiselt
"""
kutus = int(input("Sisesta liitrid: "))
km = int(input("Sisesta läbitud dist: "))
kutuse_kulu = kutus / (km / 100)
print("Kutuse_kulu:",kutuse_kulu)


"""
Arvusüsteemid
    Kasutaja sisestab täisarvu kümnendsüsteemis
    Sinu programm teisendab selle 2nd ja 16nd süsteemi
"""
arv = int(input("Sisesta arv: "))
bii = bin(arv)
heks = hex(arv)
print(bii,heks)

"""
Ajateisendus
    Kasutaja sisestab aja minutites
    Sinu valem leiab ja väljastab tunnid ja minutid
    Näiteks: sisestus 72, vastus 1:12
"""
minutid = int(input("Sisesta aeg minutites: "))
h = minutid // 60
m = minutid % 60
print(h,":",m)

"""
Leia kolmnurga hüpotenuus
    Kolmnurga külgede pikkused on a=16 ja b=9
    Kasuta Pythagorase teoreemi (a2 + b2 = c2) ja leia kolmnurga hüpotenuus
"""
a,b = 16,9
c = round(sqrt(a**2 + b**2),2)
print("Kolmnurga hüpotenuus on",c)


"""
Rulluisutajad
    Rulluisutaja keskmine kiirus on 29,9km/h
    Kui kaugele jõuab 24minutiga
"""
kiirus = 29.9
aeg = 24
distants = round(kiirus / 60 * aeg, 2)
print("Kiirusega", kiirus, "km/h jõuab",distants,"km kaugusele")


"""
Pitsa
    Võtsite 3 sõbraga suure pitsa hinnaga 12,90€
    Jätate teenindajale 10% jootraha
    Koosta programm, mis leiab kui palju peab igaüks maksma
"""
hind = 12.9
tipp = 0.1
sopru = 3
vastus = (hind + hind * tipp) / sopru
print("Igaüks peab maksma:",vastus)


"""
Toote hind
    Toote hind 36,75€
    Soodushind hetkel 40%
    Soovin kolme toote summat
"""
hind = 36.75
ale = 0.4
kogus = 3
summa = (hind-hind*ale)*kogus

print(str(kogus)+" toote hind on kokku "+str(summa))

"""
Arvutame kolmnurga ümbermõõdu
    Loo kolm täisarvulist muutujat a, b, c
    Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
"""
a, b, c = 5, 10, 15
p = a + b + c
print("Kolmnurga ümbermõõt:",p)
