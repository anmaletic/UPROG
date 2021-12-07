# Zadatak 6
# Stvorite listu boje jednostavnim nabrajanjem 6 elemenata, tj. 6 boja. Ispišite sve elemente. 
# Dodajte novu boju na kraj liste (append), umetnite novu boju na treće mjesto (insert), izbacite neku od 
# boja u listi navođenjem vrijednosti (remove), pobrišite zadnji element i element na indeksu 3 
# metodom pop i pobrisane vrijednosti sačuvajte u varijablama. Pobrišite neki element (ili više slijednih 
# elemenata) pomoću funkcije del. Sortirajte sve elementa liste (sort), obrnite redoslijed elemenata 
# (reverse). Nakon svake promijene na listi ispisati listu da se vidi učinak izvršenja pojedinih naredbi.

listaBoja = ["Crna", "Plava", "Zelena", "Zuta", "Crvena", "Bijela"]
print(*listaBoja)

listaBoja.append("Ljubicasta")
listaBoja.insert(2, "Roza")
print(*listaBoja)

listaBoja.remove("Zelena")
print(*listaBoja)

bojaZadnja = listaBoja.pop()
bojaTri = listaBoja.pop(3)
print(*listaBoja)
print(bojaZadnja)
print(bojaTri)

del(listaBoja[4])
print(*listaBoja)

listaBoja.sort()
print(*listaBoja)

listaBoja.reverse()
print(*listaBoja)