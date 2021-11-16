# Napišite program za pretvorbu vrijednosti temperature izražene u stupnjevima celzijusa (°C ) u
# farenhajte (°F) i kelvine (K)
# Modul se sastoji od 3 funkcije: main, izracunaj_kelvine i izracunaj_farenhajte.
# U main funkciji se u lokalnu varijablu učitava temperatura u °C, pozivaju se funkcije koje vraćaju
# vrijednost temperature u °F-a i K-a i te se vrijednosti ispisuju. Ovo se ponavlja dok god je unesena
# temperatura iznad nule. 

def izracunaj_Kelvine(temp):
    '''Vraca unesenu temperaturu u Kelvinima.'''
    return temp + 273.15
    

def izracunaj_Farenhajte(temp):
    '''Vraca unesenu temperaturu u Farenhajtima.'''
    return temp * 1.8 + 32

def main():
    '''Glavni program.'''
    while True:        
        unosTemp = float(input("Unesite temperaturu u *C: "))
        if(unosTemp <= 0):
            break

        print()

        print(F"{unosTemp} *C = {round(izracunaj_Farenhajte(unosTemp), 2)} *F")
        print(F"{unosTemp} *C = {round(izracunaj_Kelvine(unosTemp), 2)} *K")
        print()

main()
    