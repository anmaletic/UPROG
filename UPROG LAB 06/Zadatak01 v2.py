# Zadatak 1 – funkcija koja ne vraća vrijednost - izračun površine i dijagonale
#             pravokutnika, naredba import
# Napišite program za izračun površine i dijagonale pravokutnika. Površinu i dijagonalu izračunava i 
# ispisuje bezparametarska funkcija pravokutnik. 
# U glavnom programu unose se vrijednosti stranica i poziva se funkcija.
# Omogućite ponavljanje izvršavanja sve dok korisnik za vrijednosti stranica unosi pozitivne brojeve.
from math import sqrt

def pravokutnik(p_unosA, p_unosB):
    povrsina = p_unosA * p_unosB
    dijagonala = round(sqrt(p_unosA**2 + p_unosB**2), 2)

    print(F"P = {povrsina}")
    print(F"d = {dijagonala}")

loop = True

while loop:
    unosA = float(input("stranica a = "))
    unosB = float(input("stranica b = "))

    pravokutnik(unosA, unosB)

    if(unosA < 0 or unosB < 0):
        loop = False