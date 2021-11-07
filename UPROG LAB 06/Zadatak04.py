# Zadatak 4 – prosti brojevi

# Napišite program koji učitava prirodne brojeve sve dok se ne učita prost broj. Tada se ispisuje poruka 
# nakon koliko brojeva je učitan taj broj (npr. „Prost broj 11 učitan je nakon 8 složenih brojeva“ ili neka 
# slična poruka) .
# Svaki učitani broj šalje se na provjeru funkciji provjera_prost . Funkcija vraća True ako je broj prost, 
# inače vraća False.
# Prost broj je prirodni broj veći od 1, djeljiv jedino sa brojem 1 i sa samim sobom.

def provjera_prost(p_broj):
    dCount = 0
    for i in range(1, p_broj +1):
        if(p_broj % i == 0):
            dCount += 1
        
        if(dCount > 2):
            return False

    return True

unosCount = 0

unosBroj = int(input("Unesite prirodan broj: "))

while not provjera_prost(unosBroj):
    unosBroj = int(input("Unesite prirodan broj: "))
    unosCount += 1 

print(F"Prost broj {unosBroj} učitan je nakon {unosCount} složenih brojeva.")