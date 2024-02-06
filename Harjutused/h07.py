#Funktsioonid
#05.12.23
#S.Heinsaar
import math

def tervita(nimi, keel="de"):
    if keel == "en":
        print(f"Hi {nimi}!")
    elif keel == "et":
        print(f"Tere {nimi}!")
    else:
        print(f"Hallo {nimi}!")


tervita("Mario", "en")
tervita("Mario")


def kuup():
    a = input("Sisesta külje mõõt: ")
    v = int(a)**3
    print(v)


def kera():
    R = input("Sisesta kera raadius: ")
    S = (4*math.pi*int(R)*int(R)*int(R))/3
    print(S)


def koonus():
    r = input("Koonuse põhja raadius: ")
    h = input("Koonuse kõrgus: ")
    S = math.pi*(int(r)*int(r))
    V = (1/3)*(S*int(h))
    print(V)


def silinder():
    r = input("Sisesta silindri põhja raadius: ")
    h = input("Sisesta silindri kõrgus: ")
    S = round(math.pi*(int(r)*int(r)), 2)
    V = S*int(h)
    print(V)


def menuu():
    loop = 1