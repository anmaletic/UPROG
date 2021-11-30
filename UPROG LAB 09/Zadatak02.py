# Zadatak 2 – ugrađena metoda upper
# Napišite program koji će unositi jednu rečenicu i ispisivati sve znakove te rečenice jedan 
# ispod drugog velikim slovima. 
# Koristite for petlju (for i in recenica)

unosRecenica = input("Unesite recenicu: ")

for i in unosRecenica.upper():
    print(i)