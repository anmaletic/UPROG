# Zadatak 1 – pozitivni i negativni indeksi
# Napisati program za unos n brojeva u listu, pri čemu n mora biti paran. Ako nije, ponoviti unos. Nakon unosa
# n brojeva ispisati zbroj prvog i zadnjeg elementa, pa drugog i predzadnjeg itd.

unosN = 1

while unosN % 2 != 0:
    unosN = int(input("Unesite PARAN broj elemenata liste: "))

listaBrojeva = list(int(input(F"Unesite {i+1}. broj: ")) for i in range(unosN))

print(listaBrojeva)

for i in range(unosN // 2):
    print(F"{listaBrojeva[i]} + {listaBrojeva[-(i+1)]} = {listaBrojeva[i] + listaBrojeva[-(i+1)]}")