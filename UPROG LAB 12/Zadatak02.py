# Zadatak 2 – metoda split
# Korisnik unosi rečenicu sa završnim znakom. Operatorom in provjerava se zadnji znak i ako ga nema, 
# zahtijeva se unos samo tog zadnjeg znaka koji se dodaje na kraj unesenog teksta. Potom se sva slova 
# pretvaraju u mala, uklanja se zadnji znak i ta se promjena sprema u novu varijablu. Takva rečenica pretvara 
# se u listu riječi(lista = s.split(' ')) i lista se ispisuje. Ispisuje se i broj riječi u rečenici te riječi jedna ispod druge.

unosTekst = input("Unesite neki tekst: ")

if unosTekst[-1] not in ".!?":
    unosZnak = input("Unesite '.', '!' ili '?': ")
    unosTekst = unosTekst + unosZnak
print(unosTekst)

noviTekst = unosTekst.lower()[0:-1]
print(noviTekst)

listTekst = noviTekst.split()
print(listTekst)

print(F"Broj riječi u rečenici: {len(listTekst)}")

for rijec in listTekst:
    print(rijec)