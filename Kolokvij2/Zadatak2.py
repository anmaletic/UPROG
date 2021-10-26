# Napisati program koji broji koliko je od učitanih brojeve imalo zadnju znamenku 5. Za 
# ponavljajući unos brojeva koristiti while petlju. Unos se prekida kad korisnik upiše nulu. Po 
# izlasku iz petlje ispisuje se koliko je bilo takvih brojeva.

zadnjaZnamenka5Count = 0

while True:
    unosBroj = float(input("Unesite broj: "))
    if(unosBroj == 0):
        break
    elif(unosBroj % 10 == 5):
        zadnjaZnamenka5Count += 1

print(F"Uneseneno je {zadnjaZnamenka5Count} brojeva sa zadnjom znamenkom 5.")