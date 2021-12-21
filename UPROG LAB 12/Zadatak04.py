# Zadatak 4
# Kreirajte praznu listu proizvodi . Zatim u while petlji unosite naziv, cijenu i količinu proizvoda u pripadajuće 
# varijable. Dodajte te vrijednosti kao listu unutar liste proizvodi (proizvodi.append([naziv, cijena, kolicina]). 
# Unos se prekida kada ne unesete naziv. Dobili ste dvodimenzionalnu listu. Ispišite tabelarno unesene 
# podatke.
# Koristite for petlju koja ima varijablu 'šetalicu' po listi. Kad ta varijabla, npr. i, poprimi vrijednost prvog 
# elementa liste, taj element je zapravo lista od tri elementa - [naziv, cijena, kolicina] i[0] - naziv, i[1] - cijena, 
# i[2] - kolicina. 
# Ako želite, možete i na drugi način obaviti ispis – for petlja čija varijabla poprima vrijednosti indeksa. U tom 
# slučaju do pojedinog podatka dolazite navođenjem dva indeksa: slog[i][0],slog[i][1],slog[i][2] itd.

proizvodi = []
proizvodi.append(["brasno", 23.4, 100])
proizvodi.append(["riža", 5.7, 2])
proizvodi.append(["cedevita", 124.98, 23])
proizvodi.append(["brasno", 124.4, 123])
proizvodi.append(["riža", 1.45,  67])
proizvodi.append(["cedevita", 456.7, 32])


while True:
    unosNaziv = input("Unesite naziv proizvoda: ")
    if(unosNaziv == ""):
        break
    unosCijena = float(input("Unesite cijenu proizvoda: "))
    unosKomada = int(input("Broj komada na skladištu: "))
    proizvodi.append([unosNaziv, unosCijena, unosKomada])

#title = "naziv\t\tcijena\t\tkoličina"
index1 = 20
index2 = 20

title = "naziv" + " " * (index1 - len("cijena")) + "cijena" + " " * (index2 - len("kolicina")) + "količina"
print(title)
print("_" * len(title))


for item in proizvodi:
    row = item[0] + " " * (3 + index1 - len(item[0]) - len(str(item[1]))) + F"{round(item[1], 2)}kn" + " " * (index2 - len(str(item[2]))) + F"{item[2]}"
    print(row)