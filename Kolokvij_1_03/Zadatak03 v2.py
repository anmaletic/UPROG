# Napišite program koji traži od korisnika unos dva cijela broja veća od nule. Unos se ponavlja 
# ukoliko brojevi nisu 'dobri'. Potom se ispisuju rezultat cjelobrojnog dijeljenja i ostatak 
# cjelobrojnog dijeljenja ta dva broja. Koristite while petlju, naredbu break i funkciju 
# divmod().

unos = [2]

while True:
    unos1 = int(input("Unesite prvi pozitivni cijeli broj: "))
    unos2 = int(input("Unesite drugi pozitivni cijeli broj: "))

    if(unos1 > 0 and unos2 > 0):
        result = divmod(unos1, unos2)

        print(F"Rezultat cijelobrojnog dijeljenja: {result[0]}")
        print(F"Ostatak cijelobrojnog dijeljenja: {result[1]}")
        break

    else:
        print("Upisani brojevi nisu dobri!")