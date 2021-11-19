# Napišite program koji računa najveći zajednički dijelitelj dvaju cijelih brojeva. Unos brojeva 
# je u glavnom programu. Omogućite ponavljanje izvođenja programa sve dok korisnik ne 
# unese nulu. Definirajte funkciju koja prihvaća dvije cjelobrojne vrijednosti, te vraća njihov 
# najveći zajednički djelitelj. Najveći zajednički djelitelj dvaju cijelih brojeva je najveći cijeli 
# broj koji ih dijeli bez ostatka. 
# Ispis rezultata je u glavnom programu i npr. za brojeve 24 i 9 treba izgledati ovako:
# NZD(24, 9) = 3

def GetDjelitelj(x, y):

    if(x < y):
        iRange = x
    else:
        iRange = y

    for i in range(iRange):
        d = i + 1
        if(x % d == 0 and y % d == 0):
            _nzd = d            

    return _nzd

unosBrojX = int(input("Upisite prvi broj: "))
unosBroyY = int(input("Upisite drugi broj: "))

nzd = GetDjelitelj(unosBrojX, unosBroyY)

print(F"NZD({unosBrojX}, {unosBroyY}) = {nzd}")

# 456 96