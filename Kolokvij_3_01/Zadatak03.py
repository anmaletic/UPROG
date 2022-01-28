# 3. 
# Napišite program koji će unositi prirodan broj n, a zatim listu od n cijelih brojeva. Program 
# treba ispisati sve pozitivne elemente liste.

def printPositive(lista:list):
    listaPos = []
    for num in lista:
        if(num % 2 == 0):
            listaPos.append(num)
    print(F"Lista pozitivnih brojeva: {str(listaPos)[1:-1]}")

def main():
    unosCount = int(input("Koliko ce brojeva biti upisano? "))

    listUnos = [int(input(F"Unesite {i+1}. broj: ")) for i in range(unosCount)]

    printPositive(listUnos)

main()