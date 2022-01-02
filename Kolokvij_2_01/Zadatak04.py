# Ispravite greške (prepišite kod ali bez grešaka) tako da dobijete program koji ispisuje 
# udaljenost točke od ishodišta:

import math

def udaljenost(x,y):
    return math.sqrt(x**2 + y**2)

def main():
    kx = float(input("Unesite koordinatu x: "))
    ky = float(input("Unesite koordinatu x: "))

    print("Udaljenost t({}, {}) od ishodišta je {}.".format(kx, ky, round(udaljenost(kx, ky), 2)))

main()