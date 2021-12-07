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

    return True if otvoreneZagrade == zatvoreneZagrade else False

def tip_rezultata(izraz):
    if(izraz.find(".") > -1 or izraz.find("/") > -1):
        return float
    else:
        return int

def provjeri_zagradeCount(izraz):
    return True if izraz.count("(") == izraz.count(")") else False

def tip_rezultataCount(izraz):
    if(izraz.count(".") or izraz.count("/")):
        return float
    else:
        return int

def main():
    unosIzraz = input("Unesite aritmetički izraz: ")

#   a)
    rez = "je" if provjeri_zagrade(unosIzraz) else "nije"

    print(F"Broj zagrada {rez} isti.")
    print(F"Tip rezultata je {tip_rezultata(unosIzraz)}")

#   b)
    rez = "je" if provjeri_zagradeCount(unosIzraz) else "nije"

    print(F"Broj zagrada {rez} isti.")
    print(F"Tip rezultata je {tip_rezultataCount(unosIzraz)}")

main()