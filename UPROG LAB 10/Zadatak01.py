# Zadatak 1 – for petlja, funkcija len, izrezivanje niza (slicing), operator uvišestručenja *
# Napišite program koji će unositi neko ime te potom ispisivati to ime na sljedeći način:
# Koristite samo jednu for petlju, jednu naredbu ispisa i operator * za razmake (npr. 5 * ' ')



def ispis(ime):
    for i in range(len(ime)):
        pocetak = ime[0:i+1]
        kraj = ime[(len(ime) - (i+1))::]
        slovo = ime[len(ime) - (i+1)].upper()
        print(pocetak, " " * 5, kraj, " " * 5, slovo)

def main():
    unosIme = input("Unesite ime: ")
    ispis(unosIme)
main()