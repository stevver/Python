#Stever Heinsaar
#21.11.2023
#Ülesanne 04
import random

"""
Paaris ja paaritu
    Loo tsükkel, mis genereerib arvud 1-10 koos vastava tekstiga, kas arv on paaris või paaritu
"""
for x in range(1,11):
    if x % 2 == 0:
        v = "paaris"
    else:
        v = "paaritu"
    print(x,v)


"""
Loto
    Koosta tsükli abil programm, mis kuvab 5 suvalist  ühekohalist numbrit. Näiteks 53542
"""
for i in range(5):
    print(random.randint(0,9),end="")

print()

"""
Tärnid
    Loo tsükkel, mis väljastab 5×5 tärnid
    Loo tsükkel, mis väljastab tärnidest kasvava kolmnurga
    Loo tsükkel, mis väljastab tärnidest kahaneva kolmnurga
"""
j = 5
for i in range(5):
    print("* "*j)
    j = j - 1

print()

j = 5
for i in range(j):
    print("* "*(i+1))

print()

j = 5
for i in range(j):
    print("* "*j)



"""
Jalgpalli meeskond
    Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.
    Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.
    Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita
"""
sugu = "mees"
if sugu == "mees":
    vanus = 18
    if vanus >= 16 and vanus <= 18:
        print("Tere tulemast meeskonda!")
    else:
        print("Vanus ei sobi")
else:
    print("Muuda sugu")


"""
Müük
    Kasutaja sisestab toote hinna. Kui see on hinnaga kuni 10€, saab ta allahindlust 10%. Üle 10€ tooted saavad soodukat 20%.
    Kuva toote lõplik hind. Plokkskeemi pole vaja!
"""
hind = 20
if hind <= 10:
    soodus = 0.1
else:
    soodus = 0.2
print(f"Sinu soodus hind on: ",hind - (hind * soodus))


"""
Juubel
    Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
    Plokkskeemi pole vaja!
"""
v = 30
if v % 5 == 0:
    vastus = "on"
else:
    vastus = "ei ole"
print(f"Vanus {v}: {vastus} juubel")


"""
Matemaatika
    Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
    Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
"""
nr1 = int(input("arv1: "))
nr2 = int(input("arv2: "))
tehe = input("Vali tehe + - * /: ")

if tehe == "+":
    vastus = nr1 + nr2
elif tehe == "-":
    vastus = nr1 - nr2
elif tehe == "*":
    vastus = nr1 * nr2
elif tehe == "/":
    vastus = nr1 / nr2
else:
    vastus ="Ära pulli mees!"
    
print (f"{nr1} {tehe} {nr2} = {vastus}")


"""
Ruut
    Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
    Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
"""
nr1 = int(input("Ruudu esimene külg: "))
nr2 = int(input("Ruudu teine külg: "))

if nr1 == nr2:
    print("ruut")
else:
    print("vale kujund")