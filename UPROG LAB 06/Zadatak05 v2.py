# Zadatak 5 - broj ponavljanja zadane znamenke u broju 

# Napišite funkciju koja će prebrojati koliko se puta zadana znamenka pojavljuje u nenegativnom 
# cijelom broju i taj podatak vratiti. Funkcija ima dva parametra, za broj i znamenku. Broj i znamenka 
# unose se u glavnom programu i prosljeđuju se funkcija broji_znamenke. Omogućite ponavljanje unosa 
# brojeva sve dok korisnik ne unese negativan broj.
# Npr. za unos 4558 i 5 funkcija vraća 2, za 10000 i 0 vraća 4, za 1234 i 5 vraća 0.


def broji_znamenke(p_broj, p_znamenka):
    count = 0
    while p_broj > 0:
        if(p_broj % 10 == p_znamenka):
            count += 1
        p_broj = p_broj // 10
    return count

while True:
    unosBroj = int(input("Unesite nenegativan broj: "))

    if(unosBroj >= 0):
        unosZnamenka = int(input("Unesite znamenku: "))
            
        brojPonavljanja =  broji_znamenke(unosBroj, unosZnamenka)

        print(F"U broju {unosBroj} znamenka {unosZnamenka} se ponavlja {brojPonavljanja} puta!")
    else:
        break