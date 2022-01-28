# 6. 
# Napišite program za unos bodova iz ispita za n studenata. Bodovi se unose u listu bodovi
# preko indeksa. Ispisuje se prosječna, maksimalna i minimalna vrijednost bodova. 
# Nemojte koristiti funkciju sum pri izračunu prosjeka.

def main():
    unosCount = int(input("Koliko je studenata izaslo na ispit? "))

    bodSum = 0
    bodProsjek = 0

    for i in range(unosCount):
        unosBod = int(input(F"Unesite bodove {i+1}. studenta: "))

        if i == 0:
            bodMin = unosBod
            bodMax = unosBod

        if bodMin > unosBod:
            bodMin = unosBod
        elif bodMax < unosBod:
            bodMax = unosBod

        bodSum += unosBod

    bodProsjek = round(bodSum / unosCount, 2)

    print(F"Min: {bodMin}")
    print(F"Max: {bodMax}")
    print(F"Prosjek: {bodProsjek}")

main()