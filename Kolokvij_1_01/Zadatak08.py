# Definirajte funkciju koja će provjeriti je li neki cijeli broj prost. Unos brojeva je u funkciji 
# main. Svaki uneseni broj se provjerava – ako je 0 ili 1 unos se prekida i program završava. 
# Ako je broj 'dobar' šalje se funkciji. Funkcija vraća True ako je broj prost, inače vraća False. 
# Vraćena vrijednost se ispisuje.


def CheckIfProst(unos):
    _djelitelji = 0

    for i in range(unos):
        if(unos % (i+1) == 0):
            _djelitelji += 1

        if(_djelitelji > 2):
            _isProst = False
            break
        else:
            _isProst = True

    return _isProst


unosBroj = int(input("Unesite broj: "))

if(unosBroj > 1):
    IsProst = CheckIfProst(unosBroj)

    if(IsProst):
        print(F"{IsProst}")
    else:
        print(F"{IsProst}")