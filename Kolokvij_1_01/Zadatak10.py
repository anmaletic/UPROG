# Napišite program za izračun površine i opseg pravokutnika. Unos stranica je u funkciji main. 
# Površinu računa funkcija povrsina, a opseg funkcija opseg. Obje funkcije vraćaju izračunate 
# vrijednosti koje se potom ispisuju. Omogućite ponavljanje izvršavanja sve dok korisnik za 
# vrijednosti stranica unosi pozitivne brojeve.
# O = 2(a+b); P = ab

def Opseg(a, b):
    return 2 * (a + b)

def Povrsina(a, b):
    return a * b

_loop = True

while _loop:
    unosStranicaA = int(input("Unesite duljinu stranice a: "))
    unosStranicaB = int(input("Unesite duljinu stranice b: "))

    if(unosStranicaA > 0 and unosStranicaB > 0):

        opseg = Opseg(unosStranicaA, unosStranicaB)
        povrsina = Povrsina(unosStranicaA, unosStranicaB)

        print(F"Opseg: {opseg}")
        print(F"Površina: {povrsina}")

    else:
        _loop = False