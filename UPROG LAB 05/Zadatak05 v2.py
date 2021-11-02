# Zadatak 5 – for petlja unutar for petlje – ugnježđena petlja
# Napišite program za računanje i ispis faktorijela do unesenog broja.
# Podrazumijeva se da je korisnik unio prirodan broj.
# Napomene:
#   - Posebno izdvojite slučaj kad se ispisuje 1!
#   - U vanjskoj for petlji brojač i ide od 2 do n+1, računa se i! i vrši se ispis 
#     print('{}!='.format(i),end='')
#   - U unutarnjoj petlji brojač j ide od 1 do i+1, ispisuje se j i provjerava se da li treba 
#     ispisati '*'

import math

unosBrojFaktorijela = int(input("Unesite broj do kojeg ce se racunati faktorijeli: "))

print("1!=1")
for i in range(2, unosBrojFaktorijela+1):

    print(F"{i}!=", end="")

    for j in range(1, i+1):
        print(F"{j}", end="")
        if(j != i):
            print("*", end="")
        else:
            print("=", end="")
    print(math.factorial(i))