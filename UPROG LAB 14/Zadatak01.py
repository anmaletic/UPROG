# Zadatak 1
# Kreirajte klasu Predmet koja ima atribute naziv, ects, ukupnoSati. Koristite predefiniranu metodu __init__
# (konstruktor) za inicijalizaciju svih atributa. Definirajte metodu samostalanRad koja vraća broj sati koje
# student mora samostalno odraditi za taj predmet (ects * 30 – ukupnosati). Stvorite objekt predmet1 i unesite
# vrijednosti atributa. Ispišite sve podatke, uključujući i povratnu vrijednost metode samostalanRad.

class Predmet():
    def __init__(self, naziv, ects, ukupnoSati):
        self.naziv = naziv
        self.ects = ects
        self.ukupnoSati = ukupnoSati
    
    def samostalanRad(self):
        return self.ects * 30 - self.ukupnoSati

def main():
    predmet1 = Predmet("UPROG", 8, 90)
    print()
    print(F"Naziv: {predmet1.naziv}")
    print(F"Ects:  {predmet1.ects}")
    print(F"Ukupno sati: {predmet1.ukupnoSati}")
    print(F"Samostalan rad: {predmet1.samostalanRad()}")

main()