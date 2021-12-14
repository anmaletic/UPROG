# Zadatak 3
# Napisati program koji traži od korisnika unos prirodnog broja n. Taj broj određuje koliko će 
# elemenata imati lista. Svi elementi su cijeli brojevi. Nakon unosa brojeva u listu, lista se ispisuje. 
# Potom se ispisuje suma svih elemenata liste te najveći i najmanji broj u listi (funkcija main). 
# Definirajte funkciju koja će preko parametra primiti tu listu, izračunati prosječnu vrijednost liste i 
# nakon toga svaki broj koji je manji od prosječne vrijednosti ukloniti iz liste. Funkcija ispisuje podatak 
# koliko je brojeva pobrisano i listu svih pobrisanih vrijednosti. Nakon poziva funkcije ponovo ispišite 
# listu. Da li se lista promijenila? Objasnite taj novi ispis.



def obradaListe(lista):
    avg = sum(lista) / len(lista)
    i = 0
    count = 0
    izbrisaniBrojevi = []
    while i < len(lista):
        if lista[i] < avg:
            izbrisaniBrojevi.append(lista.pop(i))
            count += 1
        else:
            i += 1

    print(avg)
    print(izbrisaniBrojevi)
    print(count)



def main():
    unosN = int(input("Unesite broj elemenata: "))

    listaBrojeva = list(int(input(F"Unesite {i+1}. broj: ")) for i in range (unosN))

    print(F"Pocetna lista: {listaBrojeva}")

    print(F"Suma: {sum(listaBrojeva)}")
    print(F"Max: {max(listaBrojeva)}")
    print(F"Min: {min(listaBrojeva)}")

    obradaListe(listaBrojeva)
main()
