# Definirajte funkciju koja prima dva cijela broja a vraća ostatak i rezultat cjelobrojnog 
# dijeljenja većeg broja sa manjim (nemojte koristiti funkciju divmod). U funkciji main unose 
# se ta dva broja i ispisuju rezultati.

def Izracun(a, b):
    rez = a // b
    ost = a % b

    return rez, ost

def main():
    unosA = int(input("Unesite 1. broj: "))
    unosB = int(input("Unesite 2. broj: "))
    
    if unosA < unosB:
        unosA, unosB = unosB, unosA

    rezultat = Izracun(unosA, unosB)

    print(F"{unosA} / {unosB} =  {rezultat[0]} i ostatak {rezultat[1]}")

main()