#Stever Heinsaar
#20.02.2024
#Tkinter KT

from tkinter import *
from tkinter import ttk
import random
from tkinter import END
from tkinter.ttk import Treeview

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
aken.geometry("1500x800")
#aken.state("zoomed")

#Andmete sisestamine

tekst = Label(aken, text="Sisesta osaleja andmed: ")
tekst.grid(row=0, columnspan=2, pady=7)

Nime_teskt = Label(aken, text="Nimi: ")
Nime_teskt.grid(row=1, column=0, pady=7)

Nime_nimi = Entry(aken)
Nime_nimi.grid(row=1, column=1, pady=7)

Asutus_tekst = Label(aken, text="Asutus: ")
Asutus_tekst.grid(row=2, column=0, pady=7)

Asutus_nimi = Entry(aken)
Asutus_nimi.grid(row=2, column=1, pady=7)

e_posti_tekst = Label(aken, text="E-posti aadress: ")
e_posti_tekst.grid(row=3, column=0, pady=7)

e_posti_nimi = Entry(aken)
e_posti_nimi.grid(row=3, column=1, pady=7)

telefoni_tekst = Label(aken, text="Telefoni number: ")
telefoni_tekst.grid(row=4, column=0, pady=7)

telefoni_nimi = Entry(aken)
telefoni_nimi.grid(row=4, column=1, pady=7)

esitluse_tekst = Label(aken, text="Esitluse pealkiri: ")
esitluse_tekst.grid(row=5, column=0, pady=7)

esitluse_nimi = Entry(aken)
esitluse_nimi.grid(row=5, column=1, pady=7)

def registreerimis_ID():
    used_numbers = set()
    while True:
        number = str(random.randint(0000000000, 9999999999))
        if number not in used_numbers:
            used_numbers.add(number)
            return number

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
        fail.write(f"{full_name},{asutus},{e_posti},{telefoni},{esitluse},{registreerimis}\n")

def kustuta_sisestus():
    Nime_nimi.delete(0, END)
    Asutus_nimi.delete(0, END)
    e_posti_nimi.delete(0, END)
    telefoni_nimi.delete(0, END)
    esitluse_nimi.delete(0, END)

reg_nupp = Button(aken, text="Registreeri", command=lambda: [registreerimis_nupp(), kustuta_sisestus()])
reg_nupp.grid(row=6, column=0, columnspan=2, pady=7)

#Andmete kuvamine

def kuvamine():
    tree = Treeview(aken)
    tree["columns"] = ("Nimi", "Asutus", "E-posti aadress", "Telefoni number", "Esitluse pealkiri", "Registreerimis-ID")
    tree.heading("#0", text="", anchor="w")
    tree.column("#0", width=0, stretch=NO)
    tree.heading("Nimi", text="Nimi")
    tree.heading("Asutus", text="Asutus")
    tree.heading("E-posti aadress", text="E-posti aadress")
    tree.heading("Telefoni number", text="Telefoni number")
    tree.heading("Esitluse pealkiri", text="Esitluse pealkiri")
    tree.heading("Registreerimis-ID", text="Registreerimis-ID")
    
    scrollbar = Scrollbar(aken, orient="vertical", command=tree.yview)
    scrollbar.grid(row=1, column=3, rowspan=7, sticky="ns")
    
    tree.configure(yscrollcommand=scrollbar.set)
    
    with open("registreerimis_andmed.txt", "r") as file:
        data = file.readlines()
    for line in data:
        values = line.strip().split(",")
        tree.insert("", END, values=(values[0], values[1], values[2], values[3], values[4], values[5]))
    tree.grid(row=1, column=2, rowspan=7, padx=30)

kuvamine_nupp = Button(aken, text="Kuva registreerimis andmed", command=kuvamine)
kuvamine_nupp.grid(row=7, column=0, columnspan=2)

#Otsimine

otsi_nupp = Button(aken, text="Otsi osalejat", command=lambda: [otsimine()])

def otsimine():
    otsi_aken = Toplevel(aken)
    otsi_aken.title("Otsi osalejat")
    otsi_aken.geometry("1250x500")

    otsi_tekst = Label(otsi_aken, text="Sisesta osaleja registreerimis-ID või muu otsingusõna:")
    otsi_tekst.grid(row=0, column=3, pady=7)

    otsi_sisestus = Entry(otsi_aken)
    otsi_sisestus.grid(row=0, column=4, pady=7)

    def otsi_nupp():
        otsi_sisestus_tekst = otsi_sisestus.get()
        with open("registreerimis_andmed.txt", "r") as fail:
            for line in fail:
                if otsi_sisestus_tekst in line:
                    kuv = Treeview(otsi_aken)
                    kuv["columns"] = ("Nimi", "Asutus", "E-posti aadress", "Telefoni number", "Esitluse pealkiri", "Registreerimis-ID")
                    kuv.heading("#0", text="", anchor="w")
                    kuv.column("#0", width=0, stretch=NO)
                    kuv.heading("Nimi", text="Nimi")
                    kuv.heading("Asutus", text="Asutus")
                    kuv.heading("E-posti aadress", text="E-posti aadress")
                    kuv.heading("Telefoni number", text="Telefoni number")
                    kuv.heading("Esitluse pealkiri", text="Esitluse pealkiri")
                    kuv.heading("Registreerimis-ID", text="Registreerimis-ID")
                    values = line.strip().split(",")
                    kuv.insert("", END, values=(values[0], values[1], values[2], values[3], values[4], values[5]))
                    kuv.grid(row=3, rowspan=2, columnspan=7, padx=25, pady=10)
                    break
            else:
                otsi_tekst = Label(otsi_aken, text="Sellist osalejat ei leitud!")
                otsi_tekst.grid(row=2, column=3, columnspan=2, pady=7)

            
    otsi_nupp = Button(otsi_aken, text="Otsi", command=otsi_nupp)
    otsi_nupp.grid(row=1, column=3, columnspan=2, pady=7)

otsi_nupp.grid(row=8, column=0, columnspan=2, pady=7)


#Andmete muutmine

def muuda():
    muuda_aken = Toplevel(aken)
    muuda_aken.title("Muuda osaleja andmeid")
    muuda_aken.geometry("1250x500")

    muuda_tekst = Label(muuda_aken, text="Sisesta osaleja registreerimis-ID, mille andmeid soovid muuta:")
    muuda_tekst.grid(row=0, column=0, pady=7)

    muuda_sisestus = Entry(muuda_aken)
    muuda_sisestus.grid(row=0, column=1, pady=7)

    def muutmine():
        muuda_sisestus_tekst = muuda_sisestus.get()
        with open("registreerimis_andmed.txt", "r") as fail:
            for line in fail:
                if muuda_sisestus_tekst in line:
                    muuda_aken = Toplevel(aken)
                    muuda_aken.title("Muuda osaleja andmeid")
                    muuda_aken.geometry("1250x500")

                    muuda_tekst = Label(muuda_aken, text="Sisesta uued osaleja andmed:")
                    muuda_tekst.grid(row=0, columnspan=2, pady=7)

                    Nime_teskt = Label(muuda_aken, text="Nimi: ")
                    Nime_teskt.grid(row=1, column=0, pady=7)

                    Nime_nimi = Entry(muuda_aken)
                    Nime_nimi.grid(row=1, column=1, pady=7)

                    Asutus_tekst = Label(muuda_aken, text="Asutus: ")
                    Asutus_tekst.grid(row=2, column=0, pady=7)

                    Asutus_nimi = Entry(muuda_aken)
                    Asutus_nimi.grid(row=2, column=1, pady=7)

                    e_posti_tekst = Label(muuda_aken, text="E-posti aadress: ")
                    e_posti_tekst.grid(row=3, column=0, pady=7)

                    e_posti_nimi = Entry(muuda_aken)
                    e_posti_nimi.grid(row=3, column=1, pady=7)

                    telefoni_tekst = Label(muuda_aken, text="Telefoni number: ")
                    telefoni_tekst.grid(row=4, column=0, pady=7)

                    telefoni_nimi = Entry(muuda_aken)
                    telefoni_nimi.grid(row=4, column=1, pady=7)

                    esitluse_tekst = Label(muuda_aken, text="Esitluse pealkiri: ")
                    esitluse_tekst.grid(row=5, column=0, pady=7)

                    esitluse_nimi = Entry(muuda_aken)
                    esitluse_nimi.grid(row=5, column=1, pady=7)

                    def muuda_nupp():
                        nimi = Nime_nimi.get()
                        asutus = Asutus_nimi.get()
                        e_posti = e_posti_nimi.get()
                        telefoni = telefoni_nimi.get()
                        esitluse = esitluse_nimi.get()
                        registreerimis = muuda_sisestus_tekst

                        with open("registreerimis_andmed.txt", "r") as fail:
                            lines = fail.readlines()
                        with open("registreerimis_andmed.txt", "w") as fail:
                            for line in lines:
                                if muuda_sisestus_tekst in line:
                                    fail.write(f"{nimi},{asutus},{e_posti},{telefoni},{esitluse},{registreerimis}\n")
                                else:
                                    fail.write(line)
                        muuda_aken.destroy()

                    muuda_nupp = Button(muuda_aken, text="Muuda", command=muuda_nupp)
                    muuda_nupp.grid(row=6, column=0, columnspan=2, pady=7)
                    break
            else:
                muuda_tekst = Label(muuda_aken, text="Sellist osalejat ei leitud!")
                muuda_tekst.grid(row=2, columnspan=2, pady=7)

    muuda_nupp = Button(muuda_aken, text="Muuda", command=muutmine)
    muuda_nupp.grid(row=1, columnspan=2, pady=7)

muuda_nupp = Button(aken, text="Muuda osaleja andmeid", command=muuda)
muuda_nupp.grid(row=9, column=0, columnspan=2)

#Andmete kustutamine

def kustuta():
    kustuta_aken = Toplevel(aken)
    kustuta_aken.title("Kustuta osaleja andmed")
    kustuta_aken.geometry("1250x500")

    kustuta_tekst = Label(kustuta_aken, text="Sisesta osaleja registreerimis-ID, mille andmed soovid kustutada:")
    kustuta_tekst.grid(row=0, column=0, pady=7)

    kustuta_sisestus = Entry(kustuta_aken)
    kustuta_sisestus.grid(row=0, column=1, pady=7)

    def kustutamine():
        kustuta_sisestus_tekst = kustuta_sisestus.get()
        with open("registreerimis_andmed.txt", "r") as fail:
            lines = fail.readlines()
        with open("registreerimis_andmed.txt", "w") as fail:
            for line in lines:
                if kustuta_sisestus_tekst not in line:
                    fail.write(line)
        kustuta_aken.destroy()

    kustuta_nupp = Button(kustuta_aken, text="Kustuta", command=kustutamine)
    kustuta_nupp.grid(row=1, columnspan=2, pady=7)

kustuta_nupp = Button(aken, text="Kustuta osaleja andmed", command=kustuta)
kustuta_nupp.grid(row=10, column=0, columnspan=2, pady=7)


aken.mainloop()