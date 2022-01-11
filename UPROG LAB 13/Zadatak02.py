# Zadatak 2 
# Kreirajte klasu Trokut koja ima tri atributa koja predstavljaju vrijednosti stranica trokuta. Koristite 
# predefiniranu metodu __init__ (konstruktor). Definirajte i metodu ProvjeraStranica koja vraća True ako 
# stranice čine trokut, u protivnom vraća False.
# Stvorite objekt nad tom klasom, unesite duljine stranice i ispišite povratnu vrijednost metode 
# ProvjeraStranica .

class Trokut:
    def __init__(self, a = 0, b = 0, c = 0):
        self.a = a
        self.b = b
        self.c = c

    def ProvjeraStranica(self):
        if(self.a + self.b > self.c):
            return True
        return False
    
def main():
    objektTrokut = Trokut(5, 7, 9)

    print(objektTrokut.ProvjeraStranica())

main()