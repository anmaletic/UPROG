# Napišite funkciju potencija koja vraća vrijednost izraza baza**eksponent.
# Npr. za bazu 2 i eksponent 3 funkcija vraća 8 ( 2*2*2). 
# Pretpostavite da su baza i eksponent pozitivne cjelobrojne vrijednosti različite od nule. 
# Napišite program koji od korisnika traži unos vrijednosti za bazu i eksponent te poziva funkciju 
# potencija i prosljeđuje joj te dvije vrijednosti. Unutar funkcije upotrijebite for petlju za 
# ponavljajuće izvođenje izraza unutar petlje. Broj ponavljanja treba biti jednak vrijednosti 
# proslijeđenog argumenta eksponent. Funkcija vraća vrijednost izračuna.

def potencija(baza, eksponent):
    pot = baza
    for i in range(eksponent-1):
        pot *= baza

    return pot

unosBaza = int(input("Unesite bazu: "))
unosEksp = int(input("Unesite eksponent: "))

result = potencija(unosBaza, unosEksp)

print(F"{unosBaza} ** {unosEksp} = {result}")