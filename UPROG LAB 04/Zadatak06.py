# Omogućite korisniku unos n brojeva. Potom se ispisuje najveći i najmanji od učitanih brojeva.

unosKolikoBrojeva = int(input("Koliko želite brojeva upisati? "))
brojMin = 0
brojMax = 0

for i in range(unosKolikoBrojeva):
    unosBroj = int(input("Unesite {}. broj: ".format(i+1)))
    if(i == 0):
        brojMin = unosBroj
        brojMax = unosBroj
    else:
        if(brojMin > unosBroj):
            brojMin = unosBroj
        elif(brojMax < unosBroj):
            brojMax = unosBroj

print("Najveci broj je {}, a najmanji {}.".format(brojMax, brojMin))