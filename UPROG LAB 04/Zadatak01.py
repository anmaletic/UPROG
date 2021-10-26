# Iz raspona od 1 do 30 ispišite u zasebnim retcima:
# - Sve brojeve u rastućem poretku
# - Sve brojeve u opadajućem poretku
# - Sve parne brojeve u rastućem poretku
# - Sve neparne brojeve u opadajućem poretku
# Zadatak riješite pomoću četiri for petlje.

for i in range(1,31):
    print(i, end=" ")

print()
for i in range(30,0,-1):
    print(i, end=" ")

print()
for i in range(2,31,2):
    print(i, end=" ")

print()
for i in range(29,0,-2):
    print(i, end=" ")