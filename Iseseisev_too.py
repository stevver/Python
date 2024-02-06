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

def pos_neg():
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

pos_neg()
"""

"""
5. Shopping list
    Create a program that will keep track of items for a shopping list.
    The program should keep asking for new items until nothing is entered (no input followed by enter/return key).
    The program should then display the full shopping list.

def shopping():
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

shopping()
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
    if kas == "luua": # Kui kasutaja sisestas "luua", siis loob (pöörab ümber)
        sona = input("Sisesta sõna/tekst: ")[::-1]
        print(sona)
    elif kas == "tõlkida": # Kui kasutaja sisestas "tõlkida", siis tõlgib (pöörab ümber)
        sona = input("Sisesta sõna/tekst: ")[::-1]
        print(sona)
    else:
        print("Vale valik. Sisesta kas luua või tõlkida.")

salakeel() # Käivitab funktsiooni
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

def kuude_temperatuur(temperatuurid):
    kuumim_paevad = {}
    
    for kuu, paevad in temperatuurid.items():
        kuumim_paev = None
        kuumim_temperatuur = float('-inf')
        
        for paev, temperatuur in paevad.items():
            if temperatuur > kuumim_temperatuur:
                kuumim_paev = paev
                kuumim_temperatuur = temperatuur
        
        kuumim_paevad[kuu] = (kuumim_paev, kuumim_temperatuur)
    
    return kuumim_paevad

temperatuurid = {
    'jaanuar': {1: -16, 2: -12, 3: -15, 4: -20, 5: 0, 6: -1, 7: -20, 8: -2, 9: -20, 10: -14, 11: -18, 12: -8, 13: 2, 14: -1, 15: -14, 16: -7, 17: -15, 18: -17, 19: -6, 20: -17, 21: -17, 22: -7, 23: 0, 24: 3, 25: -20, 26: -17, 27: -15, 28: -8, 29: -12, 30: 3},
    'veebruar': {1: -9, 2: -2, 3: -7, 4: 1, 5: -16, 6: -19, 7: -19, 8: -11, 9: -16, 10: -15, 11: -9, 12: -2, 13: -16, 14: -4, 15: -20, 16: -5, 17: -6, 18: -17, 19: -5, 20: 0, 21: -16, 22: 2, 23: 0, 24: -20, 25: -16, 26: -2, 27: -18},
    'märts': {1: 2, 2: -9, 3: -1, 4: -3, 5: -6, 6: -2, 7: 1, 8: -2, 9: -3, 10: -9, 11: -1, 12: -4, 13: 0, 14: -6, 15: -7, 16: 1, 17: 0, 18: 2, 19: -5, 20: -10, 21: 2, 22: -7, 23: -3, 24: 2, 25: -10, 26: 2, 27: -9, 28: -8, 29: -5, 30: -2},
    'aprill': {1: -5, 2: 0, 3: 10, 4: -9, 5: 0, 6: -9, 7: -8, 8: 6, 9: -5, 10: 3, 11: -1, 12: 4, 13: 9, 14: -1, 15: 2, 16: 0, 17: 10, 18: 0, 19: 5, 20: 0, 21: -10, 22: 0, 23: 6, 24: 3, 25: -6, 26: -2, 27: -10, 28: -8, 29: -2},
    'mai': {1: 12, 2: 5, 3: 8, 4: -1, 5: -2, 6: 4, 7: 10, 8: -1, 9: 7, 10: 15, 11: 7, 12: 3, 13: 6, 14: 4, 15: 10, 16: 9, 17: 13, 18: 6, 19: 14, 20: 10, 21: 14, 22: 2, 23: 6, 24: 12, 25: 15, 26: 2, 27: 14, 28: 11, 29: 9, 30: 1},
    'juuni': {1: 12, 2: 5, 3: 17, 4: 6, 5: 10, 6: 14, 7: 9, 8: 7, 9: 15, 10: 23, 11: 29, 12: 11, 13: 16, 14: 18, 15: 9, 16: 25, 17: 14, 18: 8, 19: 16, 20: 22, 21: 19, 22: 22, 23: 23, 24: 18, 25: 16, 26: 16, 27: 26, 28: 24, 29: 22},
    'juuli': {1: 15, 2: 8, 3: 21, 4: 28, 5: 18, 6: 13, 7: 9, 8: 9, 9: 8, 10: 6, 11: 8, 12: 12, 13: 12, 14: 29, 15: 28, 16: 20, 17: 6, 18: 9, 19: 12, 20: 8, 21: 14, 22: 18, 23: 14, 24: 13, 25: 23, 26: 6, 27: 24, 28: 24, 29: 17, 30: 20},
    'august': {1: 7, 2: 6, 3: 5, 4: 19, 5: 18, 6: 18, 7: 17, 8: 20, 9: 15, 10: 11, 11: 7, 12: 10, 13: 13, 14: 12, 15: 20, 16: 11, 17: 10, 18: 14, 19: 18, 20: 14, 21: 24, 22: 6, 23: 17, 24: 16, 25: 6, 26: 17, 27: 5, 28: 13, 29: 11},
    'september': {1: 21, 2: 19, 3: 21, 4: 9, 5: 13, 6: 18, 7: 6, 8: 6, 9: 20, 10: 7, 11: 25, 12: 13, 13: 8, 14: 9, 15: 14, 16: 16, 17: 19, 18: 10, 19: 7, 20: 25, 21: 7, 22: 17, 23: 16, 24: 15, 25: 17, 26: 18, 27: 15, 28: 9, 29: 19},
    'oktoober': {1: 2, 2: 2, 3: 1, 4: 5, 6: -2, 7: 5, 8: 5, 9: 2, 10: 2, 11: 2, 12: 1, 13: -2, 14: 1, 15: -2, 16: 0, 17: -2, 18: 5, 19: 4, 20: 0, 21: 1, 22: -1, 23: 2, 24: 0, 25: 2, 26: 2, 27: 2, 28: -1, 29: 1, 30: 4, 31: -1},
    'november': {1: -6, 2: -7, 3: -2, 4: -7, 5: -2, 6: -4, 7: 0, 8: -7, 9: -8, 10: -6, 11: 0, 12: -9, 13: -2, 14: -3, 15: -2, 16: 0, 17: -8, 18: -2, 19: -5, 20: -2, 21: -5, 22: -8, 23: -10, 24: 0, 25: -2, 26: -9, 27: -9, 28: -7, 29: -1},
    'detsember': {1: -15, 2: 2, 3: -11, 4: -14, 5: -15, 6: -5, 7: -5, 8: -18, 9: -18, 10: -19, 11: 0, 12: 0, 13: 2, 14: -7, 15: -16, 16: -7, 17: -4, 18: -1, 19: -1, 20: -16, 21: -18, 22: -10, 23: -3, 24: -19, 25: -6, 26: -16, 27: -16, 28: -8, 29: -2, 30: -18},
}

kuumim_paevad = kuude_temperatuur(temperatuurid)

for kuu, (paev, temperatuur) in kuumim_paevad.items():
    print(f"Kuus {kuu} oli kõige kuumem {paev}. päeval, kus temperatuuriks oli {temperatuur} °C.")
"""

"""
17. Email
    Kasutaja lisab emaili kujul enimi.pnimi@server.com
	Programm kontrollib kas email on sisestatud õigesti
	Programm tükeldab selle ja väljastab lause: Tere enimi, sinu email on server serveris ja domeeniks on sul com

def email():
    gmail = input("Sisesta email (kujul: enimi.pnimi@server.com): ")
    if "@" not in gmail:
        print("Valesti sisestatud email. @-märk puudu.")
    print("Tere", gmail.split("@")[0].split(".")[0], ", sinu email on", gmail.split("@")[1].split(".")[0], "serveris ja domeeniks on sul", gmail.split("@")[1].split(".")[1])

email()
"""