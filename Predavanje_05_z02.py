# Napišite program koji traži od korisnika unos dva cijela pozitivna broja. Unos se
# ponavlja ukoliko brojevi nisu prirodni. Potom se ispisuje rezultat cijelobrojnog
# dijeljenja i ostatak cijelobrojnog dijelenja ta dva broja. Koristite while petlju, 
# naredbu break i funkciju divmod()

unosBroj1 = int(input("Unesite prvi cijeli pozitivni broj: "))
unosBroj2 = int(input("Unesite drugi cijeli pozitivni broj: "))

while True:
    if(unosBroj1 < 1 or unosBroj2 < 1):
        print("Brojevi nisu prirodni, pokušajte ponovo.")
        unosBroj1 = int(input("Unesite prvi cijeli pozitivni broj: "))
        unosBroj2 = int(input("Unesite drugi cijeli pozitivni broj: "))
    else:
        rezultat, ostatak = divmod(unosBroj1, unosBroj2)
        print(F"Rezultat djeljenja {unosBroj1} i {unosBroj2} je {rezultat}, a ostatak {ostatak}.")
        break