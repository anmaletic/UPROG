# Napišite program koji će ispisati sve djelitelje unesenog prirodnog broja te koliko ih ima. Ukoliko 
# uneseni broj nije prirodni, unos se ponavlja (while petlja). Kada se učita prirodni broj, izlazi se iz 
# petlje i pronalaze djelitelji tog broja.
# Za traženje,ispis i prebrojavanje djelitelja koristite for strukturu ponavljanja.



while True:
    unosBroj = int(input("Unesite prirodni broj: "))

    if(unosBroj >= 1):
        break

djelitelji = []

for i in range(1, unosBroj + 1):
            if(unosBroj % i == 0):
                djelitelji.append(i)   
                
print(F"Djelitelji broja {unosBroj} su", *djelitelji)
print(F"Djelitelji broja {unosBroj} su {str(djelitelji)[1:-1]}.")       # *djelitelji ne radi za F""

print(F"Broj {unosBroj} ima {len(djelitelji)} djelitelja.")
