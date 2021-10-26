# Napisati program za ispis svih cijelih brojeva iz nekog raspona. Omogućite korisniku da unese 
# početnu i završnu cjelobrojnu vrijednost raspona. Pazite na slučaj kad je unesena početna 
# vrijednost veća od završne (korak tada mora biti negativan). 
# Koristite samo jednu for petlju.

unosPocetnaVrijednost = int(input("Unesite pocetnu vrijednost: "))
unosZavrsnaVrijednost = int(input("Unesite zavrsnu vrijednost: "))
korak = 1

if(unosPocetnaVrijednost > unosZavrsnaVrijednost):
    unosZavrsnaVrijednost = unosZavrsnaVrijednost - 1
    korak = -korak
else:
    unosZavrsnaVrijednost = unosZavrsnaVrijednost + 1

for i in range(unosPocetnaVrijednost, unosZavrsnaVrijednost, korak):
    print(i, end=" ")