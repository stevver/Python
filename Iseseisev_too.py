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
    tehe = int(input(f"Korrutus tehe: {a} * {b} = "))
    if tehe == a*b:
        print("Õige")
    else:
        print(f"Vale, õige vastus on {a*b}")

korrutamine(random.randint(1,5),random.randint(1,5))
"""

"""
3. Positiivsed ja negatiivsed
	tee kaks loendit positiivsete ja negatiivsete arvude hoidmiseks
	kasutaja sisestab 5 arvu ja programm tuvastab, kumba loendisse selle lisab
	nulli lisamisel ei tehta midagi
	väljasta mõlemad loendit
"""
positiv = []
negativ = []
for i in range(5):
    arv = int(input("Sisesta arv: "))
    if arv > 0:
        positiv.append
    if arv < 0:
        negativ.append
    if arv == 0:
        print("Ära sisesta nulli")
