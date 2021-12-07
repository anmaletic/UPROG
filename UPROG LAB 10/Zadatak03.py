# Zadatak 3– operator in
# Napisati program koji traži od korisnika unos stringa koji predstavlja aritmetički izraz sa zagradama
# npr. ((a + 2) * (c – d)) / 4. 
# Aritmetički izraz šalje se funkciji provjeri_zagrade koja provjerava je li u izrazu jednak broj otvorenih i 
# zatvorenih zagrada, te ovisno o tom vraća odgovarajuću poruku.
# Napišite još jednu funkciju tip_rezultata koja provjerava postoji li u izrazu decimalna točka, ako postoji, 
# vraća 'float', ako ne postoji, provjerava postoji li operator '/', i ako postoji vraća 'float', inače vraća 'int'.
# Zadatak riješite:
# a) bez korištenja ugrađene funkcije count
# b) koristeći funkciju count (npr. 'ananas'.count('a') vraća 3)

def provjeri_zagrade(izraz):
    otvoreneZagrade = 0
    zatvoreneZagrade = 0
    for i in range(len(izraz)):
        if izraz[i] == "(":
            otvoreneZagrade += 1
        elif izraz[i] == ")":
            zatvoreneZagrade += 1        

    return "je" if otvoreneZagrade == zatvoreneZagrade else "nije"

def tip_rezultata(izraz):
    tip = ""
    for i in range(len(izraz)):
        if izraz[i] == ".":
            tip = "float"
        elif izraz[i] == "/":
            tip = "float"
            if izraz[i+1] == "/" or izraz[i-1] == "/":
                tip = "int"
    return tip

def tip_mislav(izraz):
    if "//" in izraz and "." not in izraz:
        print("int")
    else:
        print("float")

def tip_dragana(izraz):
    izraz = izraz.replace("//", "")
    if "/" in izraz or "." in izraz:
        print("float")
    else:
        print("int")


def provjeri_zagradeCount(izraz):
    return "je" if izraz.count("(") == izraz.count(")") else "nije"

def tip_rezultataCount(izraz):
    if(izraz.count(".") or izraz.count("/")):
        return "float"
    else:
        return "int"

def main():
    unosIzraz = input("Unesite aritmetički izraz: ")

#   a)
    print(F"Broj zagrada {provjeri_zagrade(unosIzraz)} isti.")
    print(F"Tip rezultata je {tip_rezultata(unosIzraz)}")
    tip_mislav(unosIzraz)
    tip_dragana(unosIzraz)
#   b)
 #   print(F"Broj zagrada {provjeri_zagradeCount(unosIzraz)} isti.")
 #   print(F"Tip rezultata je {tip_rezultataCount(unosIzraz)}")

main()