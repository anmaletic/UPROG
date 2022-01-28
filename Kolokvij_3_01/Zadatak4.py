# 4.
# Kreirajte klasu Predmet koja ima atribute naziv, ects, ukupnosati. Koristite predefiniranu 
# metodu __init__ (konstruktor) za inicijalizaciju svih atributa. Definirajte metodu
# samostalanrad koja vraća broj sati koje student mora samostalno odraditi za taj predmet 
# (ects * 30 – ukupnosati). Stvorite objekt predmet1 i unesite vrijednosti atributa. Ispišite 
# sve podatke, uključujući i povratnu vrijednost metode samostalanrad.

class Predmet():
    def __init__(self, n, e, us):
        self.naziv = n
        self.ects = e
        self.ukupnoSati = us

    def samostalanRad(self):
        return self.ects * 30 - self.ukupnoSati

def main():
    p1 = Predmet(input("Ime predmeta: "), int(input("Bodovi: ")), int(input("Ukupno sati: ")))

    print(F"Ime predmeta: {p1.naziv}")
    print(F"Bodovi: {p1.ects}")
    print(F"Ukupno sati: {p1.ukupnoSati}")    
    print(F"Samostalan rad: {p1.samostalanRad()}")

main()