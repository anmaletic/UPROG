# Zadatak 5 – isječak znakovnog niza, funkcija len
# Korisnik unosi neki tekst i dva pozitivna cijela broja p i k. Program ispisuje koliko znakova 
# ima tekst te p prvih znakova i k zadnjih znakova.

unosTekst = input("Unesite neki tekst: ")

print(F"U tekstu ima {len(unosTekst)} znakova.")

unosPrvih = int(input("Unesite koliko zelite prvih znakova: "))
print(unosTekst[0 : unosPrvih])

unosZadnjih = int(input("Unesite koliko zelite zadnjih znakova: "))
print(unosTekst[len(unosTekst) - unosZadnjih :])