# Napišite program koji računa sumu svih brojeva između broja a i broja b. Granice raspona su
# cijeli brojevi i podrazumijeva se da je prvi broj manji od drugog. Koristite for petlju.

unosA = int(input("Unesite pocetni broj: "))
unosB = int(input("Unesite zadnji broj: "))

suma = 0

for i in range(unosA, unosB + 1):
    suma += i

print(F"Suma svih brojeva izmedu {unosA} i {unosB} je {suma}")