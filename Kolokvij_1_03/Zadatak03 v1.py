# Napišite program koji traži od korisnika unos dva cijela broja veća od nule. Unos se ponavlja 
# ukoliko brojevi nisu 'dobri'. Potom se ispisuju rezultat cjelobrojnog dijeljenja i ostatak 
# cjelobrojnog dijeljenja ta dva broja. Koristite while petlju, naredbu break i funkciju 
# divmod().

unos = [2]

while True:
    unos = [int(item) for item in input("Unesite 2 pozitivna cijela broja (odvojena razmakom): ").split()]

    if(unos[0] > 0 and unos[1] > 0):
        result = divmod(unos[0], unos[1])

        print(F"Rezultat cijelobrojnog dijeljenja: {result[0]}")
        print(F"Ostatak cijelobrojnog dijeljenja: {result[1]}")
        break

    else:
        print("Upisani brojevi nisu dobri!")