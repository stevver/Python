#Iseseisev töö 4
#10.01.24
#S.Heinsaar

"""
def banner(t):
    print(t.upper())

ask = int(input("Mitu korda: "))
ask2 = input("Reklaamlause: ")

for i in range(ask):
    banner(ask2)


#Õunamahlad
def mahlapakkide_arv(kg):
    pakkid = round(kg * 0.4 / 3)
    return pakkid

kogus = float(input("Õunte arv: "))
print(mahlapakkide_arv(kogus))


def eelarve(kylalised):
    summa = kylalised * 10 + 55
    return summa

palju = int(input("Mitu külalist on kutsutud: "))
palju2 = int(input("Mitu tuleb: "))
print(f"Maksimaalne eelarve: {eelarve(palju)}€")
print(f"Minimaalne eelarve: {eelarve(palju2)}€")


kylalisi = 3
def tervitus(n):
    print('Võõrustaja: "Tere!"')
    print(f"Täna {n}. kord tervitada!")
    print('Külaline: "Tere, suur tänu kutsumast!"')

for i in range(kylalisi):
    tervitus(i+1)
"""

#Mündid
def pronksikarva_summa(f):
    kassa = 0
    fail = open(f) 
    for mynt in fail:
        if int(mynt) < 10:
            #print(mynt)
            kassa += int(mynt)
    print("Kassas: ", kassa)


pronksikarva_summa("myndid.txt")