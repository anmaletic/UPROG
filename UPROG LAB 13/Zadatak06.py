# Zadatak 6
# Kreirajte klasu TekuciRacun koja ima atribut pocetnostanje te metode za uplatu, isplatu i prikaz 
# stanja racuna. Metoda __init__ stvara racun i postavlja pocetno stanje na difoltnu nulu. Metoda 
# uplata jednostavno povećava stanje za uneseni iznos, metoda isplata prvo provjerava ima li 
# dovoljno novca za isplatu, ako ima, umanji trenutno stanje, ako nema, javi poruku o tom.

class TekuciRacun():
    def __init__(self, pocetnostanje = 0):
        self.StanjeRacuna = pocetnostanje

    def Uplata(self, iznos):
        self.StanjeRacuna += iznos

    def Isplata(self, iznos):
        if(self.StanjeRacuna >= iznos):
            self.StanjeRacuna -= iznos
        else:
            print("Nema dovoljno novaca za isplatu!")

    def Stanje(self):
        return self.StanjeRacuna

def main():

    Racun = TekuciRacun()

    print("****************")
    print("1. Stanje računa")
    print("2. Uplata")
    print("3. Isplata")
    print("4. Završetak")
    print("****************")

    while True:
        print()
        unosOdabir = int(input("Odaberite broj 1-4: "))

        match unosOdabir:
            case 1:
                print(F"Na računu imate: {Racun.Stanje()}")
            case 2:
                unosIznos = int(input("Unesite iznos u kunama: "))
                Racun.Uplata(unosIznos)
            case 3:
                unosIznos = int(input("Unesite iznos u kunama: "))
                Racun.Isplata(unosIznos)
            case 4:
                print("Hvala i doviđenja!")
                break
            case _:
                print("Nepostojeći odabir!")

main()