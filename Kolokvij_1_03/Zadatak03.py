# Napišite program koji traži od korisnika unos dva cijela broja veća od nule. Unos se ponavlja 
# ukoliko brojevi nisu 'dobri'. Potom se ispisuju rezultat cjelobrojnog dijeljenja i ostatak 
# cjelobrojnog dijeljenja ta dva broja. Koristite while petlju, naredbu break i funkciju 
# divmod().

unos = [2]

unos = [int(item) for item in input("Unesite 2 pozitivna cijela broja (odvojena razmakom): ").split()]

print(*unos)