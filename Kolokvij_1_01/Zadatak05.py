# Napišite program koji omogućava unos cijene tepiha i materijala od kojeg je napravljen. 
# Ukoliko je cijena manja od 5000 kn i materijal vuna ili pamuk napisati ''provjeriti dimenzije'', 
# u suprotnom napisati ''ne kupujem''. Unos cijene i materijala je u glavnom programu. Za 
# provjeru unesenih podataka definirajte funkciju koja prima iznos cijene i vrstu materijala a 
# vraća odgovarajući tekst. Unutar funkcije koristite samo jednu if…else naredbu i logičke 
# operatore and i or.

def KontrolaUnosa(cijena, materijal):
    if(cijena < 5000 and (materijal == "vuna" or materijal == "pamuk")):
        return "Provjeriti dimenzije."
    else:
        return "Ne kupujem."

unosCijena = float(input("Unesite cijenu tepiha: "))
unosMaterijal = input("Unesite materijal tepiha: ")

result = KontrolaUnosa(unosCijena, unosMaterijal)

print(result)