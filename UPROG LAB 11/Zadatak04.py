# Zadatak 4
# Napisati program za unos imena i prezimena za n studenata. Prije unosa vrijednosti u listu, inicijalizirajte listu 
# na praznu listu (ime_liste = [])
# Za unos koristiti for petlju i funkciju append (ime_liste.append(input(poruka)). Ispisati listu na dva dolje 
# prikazana načina.

listaStudenata = []

unosN = int(input("Unesite broj elemenata: "))

for i in range(unosN):
    listaStudenata.append(input(F"Unesite ime i prezme {i+1}. studenta: "))

print(listaStudenata)

for i in range(len(listaStudenata)):
    print(F"{i+1}. {listaStudenata[i]}")
