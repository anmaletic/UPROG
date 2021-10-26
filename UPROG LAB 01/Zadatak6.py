
duljina_letvice = int(input("Unesite duljinu letvice: "))
duljina_dijela = int(input("Unesite duljinu dijela koji je potrebno izrezati: "))

kolicina_dijelova = duljina_letvice // duljina_dijela
kolicina_ostatak = duljina_letvice % duljina_dijela

print("Moguce je izrezati " + str(kolicina_dijelova) + " letvice, a preostat ce " + str(kolicina_ostatak))