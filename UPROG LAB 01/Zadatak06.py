# Napisati program u kojem se od korisnika traži unos duljine letvice u cm i duljine dijela koji će 
# se izrezati (isto cm). Izračunati i ispisati koliko se takvih dijelova može izrezati i koliko će 
# letvice preostati.
# Podrazumijeva se da je korisnik za vrijednosti duljina unio pozitivne cijele brojeve.

duljina_letvice = int(input("Unesite duljinu letvice: "))
duljina_dijela = int(input("Unesite duljinu dijela koji je potrebno izrezati: "))

kolicina_dijelova = duljina_letvice // duljina_dijela
kolicina_ostatak = duljina_letvice % duljina_dijela

print("Moguce je izrezati " + str(kolicina_dijelova) + " letvice, a preostat ce " + str(kolicina_ostatak))