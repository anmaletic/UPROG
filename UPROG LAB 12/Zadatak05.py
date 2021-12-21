# Zadatak 5
# Kreirajte klasu Tocka koja ima dva podatkovna atributa za koordinate neke točke. Koristite metodu 
# __init__ za inicijalizaciju atributa. Definirajte metodu udaljenost koja vraća udaljenost točke od 
# ishodišta ( √𝑥 2 + 𝑦 2).
# Instancirajte dva objekta klase Tocka. Prvom objektu pridružite vrijednosti koordinata pri stvaranju 
# objekta. Drugom objektu, nakon stvaranja objekta, unesite vrijednosti.

from math import sqrt

class Tocka():
    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b
    def udaljenost(self):
        return round(sqrt(self.x**2 + self.y**2))

t1 = Tocka(2,3)
print(t1.udaljenost())

t2 = Tocka()
t2.x = 2
t2.y = 3
print(t2.udaljenost())
