# Napišite program koji će ispisati sve djelitelje unesenog prirodnog broja te koliko ih ima. Ukoliko 
# uneseni broj nije prirodni, unos se ponavlja (while petlja). Kada se učita prirodni broj, izlazi se iz 
# petlje i pronalaze djelitelji tog broja.
# Za traženje,ispis i prebrojavanje djelitelja koristite for strukturu ponavljanja.



while True:
    unosBroj = int(input("Unesite prirodni broj: "))

    if(unosBroj >= 1):
        break

djeliteljiCount = 0

print("Djelitelji broja {} su: ".format(unosBroj), end="")

for i in range(1, unosBroj + 1):
            if(unosBroj % i == 0):
                djeliteljiCount += 1
                print(i, end=" ")

print()          
print("Broj {} ima {} djelitelja.".format(unosBroj, djeliteljiCount))
