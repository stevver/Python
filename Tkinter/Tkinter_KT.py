#Stever Heinsaar
#20.02.2024
#Tkinter KT

from tkinter import *
from tkinter import ttk
import random

"""
Konverentsi registreerimissüsteem

Eesmärk: arendada Pythoni ja Tkinteri abil rakendus, mis haldab konverentsi osalejate registreerimist. Rakendus võimaldab kasutajal sisestada, vaadata, muuta ja kustutada osalejate andmeid,
sealhulgas nime, asutust, kontaktandmeid (e-posti ja telefoninumbrit) ning esitluse pealkirja. Iga osaleja kohta genereeritakse süsteemi lisamisel unikaalne registreerimis-ID.

Funktsionaalsus:
* Andmete sisestamine: Kasutajad saavad sisestada osalejate andmeid, sealhulgas nime, asutust, kontaktandmeid ja esitluse pealkirja. Sisestamisel genereerib süsteem iga osaleja jaoks unikaalse registreerimis-ID.
* Andmete vaatamine: Rakendus kuvab nimekirja kõigist registreeritud osalejatest. Kasutajad saavad otsida osalejaid nende unikaalse registreerimis-ID või muude andmete alusel.
* Andmete muutmine ja kustutamine: Kasutajad saavad muuta olemasolevate osalejate andmeid või kustutada neid süsteemist, et hoida registreerimisinfo ajakohane.
* Andmete salvestamine: Andmed salvestatakse failisüsteemi, kasutades CSV või TXT failivormingut, mis võimaldab hõlpsat andmete haldamist ja taaskasutamist.

Nõuded:
* Kasutajaliides peab olema loodud Tkinteri abil, pakkudes lihtsat ja intuitiivset kasutajakogemust.
* Rakendus peab tagama andmete järjepidevuse ja turvalisuse, kasutades failipõhist salvestusviisi.
* Unikaalse registreerimis-ID genereerimine peab tagama, et iga osaleja ID on ainulaadne.
* Rakendus peab võimaldama osalejate andmete lihtsat sisestamist, muutmist, vaatamist ja kustutamist.
* Failid peavad olema kättesaadavad Githubis
"""

#Aken
aken = Tk()
aken.title("Konverentsi registreerimissüsteem")
aken.geometry("800x600")

#Andmete sisestamine

tekst = Label(aken, text="Sisesta osaleja andmed: ")
tekst.grid(row=0, columnspan=2)

Nime_teskt = Label(aken, text="Nimi: ")
Nime_teskt.grid(row=1, column=0)

Nime_nimi = Entry(aken)
Nime_nimi.grid(row=1, column=1)

Asutus_tekst = Label(aken, text="Asutus: ")
Asutus_tekst.grid(row=2, column=0)

Asutus_nimi = Entry(aken)
Asutus_nimi.grid(row=2, column=1)

e_posti_tekst = Label(aken, text="E-posti aadress: ")
e_posti_tekst.grid(row=3, column=0)

e_posti_nimi = Entry(aken)
e_posti_nimi.grid(row=3, column=1)

telefoni_tekst = Label(aken, text="Telefoni number: ")
telefoni_tekst.grid(row=4, column=0)

telefoni_nimi = Entry(aken)
telefoni_nimi.grid(row=4, column=1)

esitluse_tekst = Label(aken, text="Esitluse pealkiri: ")
esitluse_tekst.grid(row=5, column=0)

esitluse_nimi = Entry(aken)
esitluse_nimi.grid(row=5, column=1)

def registreerimis_ID():
    start = "0000000001"
    end = "9999999999"
    return random.randint(int(start), int(end))

def registreerimis_nupp():
    nimi = Nime_nimi.get()
    asutus = Asutus_nimi.get()
    e_posti = e_posti_nimi.get()
    telefoni = telefoni_nimi.get()
    esitluse = esitluse_nimi.get()
    registreerimis = registreerimis_ID()
    
    name_parts = nimi.split()
    
    full_name = " ".join(name_parts)
    
    print("Nimi: " + full_name + "\nAsutus: " + asutus + "\nE-posti aadress: " + e_posti + "\nTelefoni number: " + telefoni + "\nEsitluse pealkiri: " + esitluse + "\nRegistreerimis-ID: " + str(registreerimis))

    with open("registreerimis_andmed.txt", "a") as fail:
        if fail.tell() == 0:
            fail.write("Nimi,Asutus,E-posti aadress,Telefoni number,Esitluse pealkiri,Registreerimis-ID\n")
        fail.write(f"{full_name},{asutus},{e_posti},{telefoni},{esitluse},{registreerimis}\n")

reg_nupp = Button(aken, text="Registreeri", command=lambda: registreerimis_nupp())
reg_nupp.grid(row=6, column=0, columnspan=2)

#Andmete kuvamine

kuvamine = Label(aken, text="Registreeritud osalejad: ")
kuvamine.grid(row=1, column=3, columnspan=2)

def kuvamine():
    with open("registreerimis_andmed.txt", "r") as fail:
        andmed = fail.readlines()
        for rida in andmed:
            print(rida)

kuv_nupp = Button(aken, text="Kuva osalejate andmed", command=lambda: kuvamine())
kuv_nupp.grid(row=6, column=3, columnspan=2)



aken.mainloop()