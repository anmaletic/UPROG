# Iz prethodne vježbe (vj 12) riješite zadatak 4 pomoću klase.
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

class Proizvod():
    def __init__(self, naziv, cijena, kolicina):
        self.n = naziv
        self.c = cijena
        self.k = kolicina    

def main():
    proizvodi = []

    proizvodi = []
    proizvodi.append(Proizvod("brasno", 23.4, 100))
    proizvodi.append(Proizvod("riža", 5.7, 2))
    proizvodi.append(Proizvod("cedevita", 124.98, 23))
    proizvodi.append(Proizvod("brasno", 124.4, 123))
    proizvodi.append(Proizvod("riža", 1.45,  67))
    proizvodi.append(Proizvod("cedevita", 456.7, 32))
    

    while True:
        unosNaziv = input("Unesite naziv proizvoda: ")
        if(unosNaziv == ""):
            break
        unosCijena = float(input("Unesite cijenu proizvoda: "))
        unosKolicina = int(input("Unesite količinu proizvoda: "))

        proizvodi.append(Proizvod(unosNaziv, unosCijena, unosKolicina))

    index = 20

    title = "naziv" + " " * (index - len("cijena")) + "cijena" + " " * (index - len("kolicina")) + "količina"
    print(title)
    print("_" * len(title))


    for item in proizvodi:
        row = item.n + " " * (3 + index - len(item.n) - len(str(item.c))) + F"{round(item.c, 2)}kn" + " " * (index - len(str(item.k))) + F"{item.k}"
        print(row)

main()