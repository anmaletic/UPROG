# Zadatak 1 – podrazumijevani parametri, opcioni argumenti
# Napišite funkciju koja ima jedan obavezni i tri defaultna parametra (sva tri imaju 
# predefiniranu vrijednost 1). Funkcija samo ispisuje vrijednosti svojih parametara. Pozovite 
# funkciju osam puta tako da dobijete sljedeće ispise:

def ispis(p1, p2 = 1, p3 = 1, p4 = 1):
    print(p1, p2, p3, p4)

def main():
    ispis(1)
    ispis(2,p4=2)
    ispis(3, p3=2)
    ispis(4, 2)
    ispis(5, p4=5)
    ispis(1, 2, 3, 4)
    ispis(4, p3=4)
    ispis(8, 7, 6, 5)

main()