# Imate dva strujna kruga, jedan sa dva serijski spojena otpornika i drugi sa dva paralelno spojena
# otpornika. Napišite program koji će po izboru korisnika računati ukupni otpor jednog od ta dva 
# strujna kruga. 
# Program se sastoji od tri funkcije – glavne funkcije main (unos vrijednosti otpora u omima, prikaz 
# izbornika, unos izbora, poziv odgovarajuće funkcije i ispis ukupnog otpora u omima), funkcije 
# serijski_otpor i funkcije paralelni_otpor. Obje funkcije imaju po dva parametra. 
# Ukupan otpor serijski spojenih otpornika R=R1+R2
# Ukupan otpor paralelno spojenih otpornika R=R1*R2/(R1+R2).

def serijski_otpor(r1, r2):
    '''Funkcija računa ukupan otpor serijskog spoja'''
    return r1 + r2

def paralelni_otpor(r1, r2):
    '''Funkcija računa ukupan otpor paralelnog spoja'''
    return round((r1 * r2) / (r1 + r2), 2)

def main():
    while True:
        print()
        unosR1 = float(input("Unesite vrijednost otpornika R1 (u ohmima): "))
        unosR2 = float(input("Unesite vrijednost otpornika R2 (u ohmima): "))

        if(unosR1 <= 0 or unosR2 <= 0):
            break
        else:
            print()
            title = "Tip spoja:"
            print(title)
            print("-" * len(title)*2)

            print("1. Paralelni spoj")
            print("2. Serijski spoj")
            print()

            unosOdabir = int(input("Odaberite redni broj spoja: "))
            print()

#            if(unosOdabir == 1):
#                print(F"Ukupan otpor otpornika R1 = {unosR1} Ohm i R2 = {unosR2} Ohm iznosi {paralelni_otpor(unosR1, unosR2)} Ohma")
#            else:
#                print(F"Ukupan otpor otpornika R1 = {unosR1} Ohm i R2 = {unosR2} Ohm iznosi {serijski_otpor(unosR1, unosR2)} Ohma")


#           Python 3.10
            match unosOdabir:
                case 1:
                    print(F"Ukupan otpor otpornika R1 = {unosR1} Ohm i R2 = {unosR2} Ohm iznosi {paralelni_otpor(unosR1, unosR2)} Ohma")
                case 2:
                    print(F"Ukupan otpor otpornika R1 = {unosR1} Ohm i R2 = {unosR2} Ohm iznosi {serijski_otpor(unosR1, unosR2)} Ohma")

main()