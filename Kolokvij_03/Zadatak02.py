# Napisati program koji broji koliko je od učitanih brojeva negativnih. Za ponavljajući unos 
# brojeva koristiti while petlju. Unos se prekida kad korisnik upiše nulu. Po izlasku iz petlje 
# ispisuje se koliko je učitani brojeva i koliko ih je bilo negativnih.

_loop = True
loopCount = 0
negativniCount = 0

while _loop:
    loopCount += 1

    unos = int(input(F"Unesite {loopCount}. broj: "))

    if(unos == 0):
        _loop = False
    elif(unos < 0):
        negativniCount += 1

print(F"Unesenih brojeva: {loopCount}")
print(F"Negativnih brojeva: {negativniCount}")
