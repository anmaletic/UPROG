# Zadatak 1 – funkcija koja ne vraća vrijednost - izračun površine i dijagonale
#             pravokutnika, naredba import
# Napišite program za izračun površine i dijagonale pravokutnika. Površinu i dijagonalu izračunava i 
# ispisuje bezparametarska funkcija pravokutnik. 
# U glavnom programu unose se vrijednosti stranica i poziva se funkcija.
# Omogućite ponavljanje izvršavanja sve dok korisnik za vrijednosti stranica unosi pozitivne brojeve.
from math import sqrt

def pravokutnik():
    povrsina = unosA * unosB
    dijagonala = round(sqrt(unosA**2 + unosB**2), 2)

    print(F"P = {povrsina}")
    print(F"d = {dijagonala}")



while True:
    unosA = float(input("stranica a = "))
    unosB = float(input("stranica b = "))
    
    pravokutnik()

    if(unosA <= 0 or unosB <= 0):
        break

