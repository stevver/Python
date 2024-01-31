#Iseseisev töö
#S.Heinsaar
#16.01.24
import random


"""
1. Korrutamise kontrollimine
	programm esitab korrutustehte
	ootab kasutajalt vastuse sisestamist
	kontrollib vastuse õigsust
	väljastab, kas vastus oli õige või väär.
	kokku antakse lahendamiseks 10 ülesannet.


def korrutamine(a,b):
    vastus = int(input(f"{a} * {b} = "))
    if vastus == a*b:
        print("Õige vastus")
    else:
        print("Vale vastus, õige vastus on: ", a*b)

for i in range(10):
    a = random.randint(1,10)
    b = random.randint(1,10)
    korrutamine(a,b)
"""

"""
3. Positiivsed ja negatiivsed
	tee kaks loendit positiivsete ja negatiivsete arvude hoidmiseks
	kasutaja sisestab 5 arvu ja programm tuvastab, kumba loendisse selle lisab
	nulli lisamisel ei tehta midagi
	väljasta mõlemad loendit

positiv = []
negativ = []
for i in range(5):
    arv = int(input("Sisesta arv: "))
    if arv > 0:
        positiv.append(arv)
    elif arv < 0:
        negativ.append(arv)
    if arv == 0:
        print("Ära lisa nulli")
print(f"Positiivsed: {positiv}")
print(f"Negatiivsed: {negativ}")
"""

"""
5. Shopping list
    Create a program that will keep track of items for a shopping list.
    The program should keep asking for new items until nothing is entered (no input followed by enter/return key).
    The program should then display the full shopping list.

shopping_list = []
while True:
    toode = input("Sisesta toode: ")
    if toode == "":
        break
    shopping_list.append(toode)

if shopping_list:
    print("Ostu korv:")
    for toode in shopping_list:
        print(toode)
else:
    print("Ostu korv on tühi.")
"""

"""
7. Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või EEK->EUR.
	kuvatakse korrektne arusaadav küsimus ja vastus
	kuvatakse veateade, kui kasutaja tegi valiku valesti
	küsitakse valuuta kogust ja tehakse arvutused
	kood kommenteeritud

def valuuta_kalkulaator():
    kumb = input("Kas soovid EUR->EEK või EEK->EUR? ") # Küsib millist kursi soovitakse arvutada
    if kumb != "EUR->EEK" and kumb != "EEK->EUR": # Kui kasutaja siestab peale EUR->EEK või EEK->EUR midagi muud, siis annab veateate
        print("Vale valik. Sisesta kas EUR->EEK või EEK->EUR.") # Veateade
    if kumb == "EUR->EEK": #Kui muutuja "kumb" on EUR->EEK, siis:
        summa = float(input("Sisesta summa: ")) # Küsib kasutajalt summat
        print(f"{summa} eurot on {summa*15.6466} krooni.") # Arvutab summa
    if kumb == "EEK->EUR": # Kui muutuja "kumb" on EEK->EUR, siis:
        summa = float(input("Sisesta summa: ")) # Küsib kasutajalt summat
        print(f"{summa} krooni on {summa/15.6466} eurot.") # Arvutab summa

valuuta_kalkulaator() # Käivitab funktsiooni
"""

"""
9. Emaili kontroll
    kasutaja lisab emaili kujul enimi.pnimi@server.com
    programm kontrollib kas email on sisestatud õigesti - vähemalt @-märgi kontroll
	programm tükeldab selle ja väljastab lause: ‘Tere enimi, sinu email on server serveris ja domeeniks on sul com’
	kasutajalt küsitud küsimused on selgelt üheselt mõistetavad
	kood kommenteeritud

def emaili_kontroll():
    email = input("Sisesta email (kujul: enimi.pnimi@server.com): ") # Küsib kasutajalt emaili
    if "@" not in email: # Kui kasutaja ei sisesta @, siis annab veateate
        print("Vale email. Sisesta @-märk.")
    print("Tere", email.split("@")[0].split(".")[0], ", sinu email on", email.split("@")[1].split(".")[0], "serveris ja domeeniks on sul", email.split("@")[1].split(".")[1]) # Väljastab lause

emaili_kontroll()
"""

"""
11. Salakeel
    sinu programm küsib kasutajalt, kas ta soovib salakeelt luua või tõlkida
	kasutaja sisestab tavalise sõna, mis muudetakse salakeeleks
	kasutaja sisestab salakeeles sõna, mis teisendatakse jälle normaalseks
	kood kommenteeritud

def salakeel():
    kas = input("Kas soovid salakeelt luua või tõlkida? (luua/tõlkida): ") # Küsib kasutajalt, kas ta soovib salakeelt luua või tõlkida
    if kas == "luua":
        sona = input("Sisesta sõna/tekst: ")[::-1]
        print(sona)
    elif kas == "tõlkida":
        sona = input("Sisesta sõna/tekst: ")[::-1]
        print(sona)
    else:
        print("Vale valik. Sisesta kas luua või tõlkida.")

salakeel()
"""

"""
13. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
    kuvatakse korrektne arusaadav küsimus ja  vastus
	eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli
	kood mis teavitab paaris või paaritust arvust
	kuvatakse programmi pealkiri

def paaris_paaritu():
    print("Paaaris või paaritu arv?")
    print()
    try:
        arv = int(input("Sisesta arv: "))
    except ValueError:
        print("Vale sisend. (Sisesta arv.)")
        return
    if arv == 0:
        print("Ära sisesta nulli.")
        return
    if arv % 2 == 0:
        print("Arv on paaris.")
    else:
        print("Arv on paaritu.")

paaris_paaritu()
"""

"""
15. Temperatuurid
    Programm peab töötlema ühe aasta kõigi päevade temperatuure.
    Kirjutada programm, mis leiab kuude kaupa, mitmendal kuupäeval oli kõige soojem.
    Väljasta kuupäev ja vastav temperatuur. (Kui sama temperatuuriga oli mitu päeva, väljasta vähemalt üks)
"""
