# Zadatak 2
# Definirajte klasu GrupeVjezbe koja ima svojstva (atribute) oznake grupe (npr L2, L3 i sl) i listu svih studenata
# koji su u toj grupi. Definirajte metodu dodajStudenta() koja će dodati novog studenta u grupu, ali samo ako
# trenutni broj studenata u grupi nije veći od 15 (inače vraća poruku o popunjenosti grupe). Definirajte i
# metodu ispis(),koja će ispisati naziv grupe i sve studente u toj grupi (sa rednim brojem, jedan ispod drugoga,
# sortirano). U funkciji main() stvorite objekt te klase, dodajte određeni broj studenata u grupu i pozovite
# metodu ispis()

class GrupeVjezbe():
    def __init__(self, oznaka, studenti = []):
        self.oznaka = oznaka
        self.studenti = studenti

    def DodajStudenta(self, student):
        if(len(self.studenti) < 15):
            self.studenti.append(student)
        else:
            print("Nema slobodnih mjesta u grupi!")
            print()

    def Ispis(self):
        print(F"Naziv grupe: {self.oznaka}")
        
        for i in range(len(self.studenti)):
            print(F"{i+1}. {self.studenti[i]}")

def main():
    grupaL2 = GrupeVjezbe("L2")    
    grupaL2.DodajStudenta("Antonio")
    grupaL2.DodajStudenta("Mislav")
    grupaL2.DodajStudenta("Marko")
    grupaL2.DodajStudenta("Josip")
    grupaL2.DodajStudenta("Tomislav")
    grupaL2.DodajStudenta("Mladen")
    grupaL2.DodajStudenta("Antonio")
    grupaL2.DodajStudenta("Mislav")
    grupaL2.DodajStudenta("Marko")
    grupaL2.DodajStudenta("Josip")
    grupaL2.DodajStudenta("Tomislav")
    grupaL2.DodajStudenta("Mladen")
    grupaL2.DodajStudenta("Antonio")
    grupaL2.DodajStudenta("Mislav")
    grupaL2.DodajStudenta("Marko")
    grupaL2.DodajStudenta("Josip")

    grupaL2.Ispis()

main()