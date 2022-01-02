# Napisati program koji će prebrojati koliko se puta zadani znak pojavljuje u upisanome 
# znakovnom nizu. U glavnoj funkciji se unose tekst i znak i ispisuje rezultat. U funkciji 
# broji_znak se prebroje znakovi i taj se podatak vraća pozivatelju. Nemojte koristiti metodu 
# count.

def broji_znak(tekst, znak):
    count = 0
    for slovo in tekst.lower():
        if slovo == znak:
            count += 1
    return count

def main():
    unosTekst = input("Unesite tekst: ")
    unosZnak = input("Unesite znak: ")

    print(F"Znak '{unosZnak}' javlja se {broji_znak(unosTekst, unosZnak)} puta.")

main()