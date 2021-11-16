# U glavnom programu unose se dva prirodna broja (podrazumijeva se da je prvi manji od drugog) i ispisuje
# se suma svih brojeva između ta dva broja. Sumu računa i vraća funkcija koja ima dva parametra preko
# kojih prima ta dva broja. Npr. za brojeve 2 i 7 rezultat je 18.


def Suma(a, b):
    '''Vraca zbroj svih brojeva izmedu upisanih brojeva.'''
    sum = 0
    for i in range(a+1, b):
        sum += i
    return sum



unosA = int(input("Prvi prirodni broj  : "))
unosB = int(input("Drugi prirodni broj : "))

print(F"Suma svih brojeva izmedu {unosA} i {unosB} iznosi {Suma(unosA, unosB)}.")