# Napisati program za unos n brojeva. Prebrojati koliko je od tih brojeva manjih od 0, jednakih 
# nulu i većih od nule. Potom se ti podatci ispisuju. 

manjiOdNulaCount = 0
jednakiNulaCount = 0
veciOdNulaCount = 0

unosKolikoBrojeva = int(input("Koliko želite brojeva upisati? "))


for i in range(unosKolikoBrojeva):
    unosBroj = float(input(F"Unesite {i+1}. broj: "))

    if(unosBroj < 0):
        manjiOdNulaCount += 1
    elif(unosBroj == 0):
        jednakiNulaCount += 1
    else:
        veciOdNulaCount += 1

print(F"Uneseno je: \n{manjiOdNulaCount} manjih od nula \n{jednakiNulaCount} jednakih nula \n{veciOdNulaCount} vecih od nula")

