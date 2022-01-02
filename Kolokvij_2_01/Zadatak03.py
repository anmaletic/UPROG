# Napišite program za izračun površine pravokutnog trokuta. Unos vrijednosti dviju kateta je u 
# funkciji main. Površinu izračunava i ispisuje funkcija trokut. 
# Omogućite ponavljanje izvršavanja sve dok korisnik za vrijednosti kateta unosi pozitivne 
# brojeve.
# P = ab/2 
# Napomena: nemojte koristiti globalne varijable

def trokut(a, b):
    return (a*b) / 2

def main():
    while True:
        unosA = float(input("A = "))
        if(unosA <= 0):
            break
        unosB = float(input("B = "))
        if(unosB <= 0):
            break

        print(trokut(unosA, unosB))

main()