# Zadatak 1 – for petlja, funkcija len, izrezivanje niza (slicing), operator uvišestručenja *
# Napišite program koji će unositi neko ime te potom ispisivati to ime na sljedeći način:
# Koristite samo jednu for petlju, jednu naredbu ispisa i operator * za razmake (npr. 5 * ' ')



def ispis(ime):
    for i in range(1, len(ime)+1):
        pocetak = ime[0:i]
        kraj = ime[-i:]
        slovo = ime[-i].upper()
        print(pocetak, " " * 5, kraj, " " * 5, slovo)
        
def main():
    unosIme = input("Unesite ime: ")
    ispis(unosIme)
main()