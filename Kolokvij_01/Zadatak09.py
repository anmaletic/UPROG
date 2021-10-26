# Korisnik unosi cjelobrojne vrijednosti u rasponu od 1 do 100. Za svaki uneseni broj 
# provjerava se da li je u zadanom rasponu, i ako nije, ispisuje se odgovarajuća poruka i unos 
# se ponavlja. Za "dobre" brojeve računa se posebno suma parnih i broj parnih, te suma 
# neparnih i broj neparnih. Unos brojeva se prekida kada su obje sume, i parnih i neparnih 
# brojeva, veće od 100. Nakon izlaska iz petlje ispisuju se podatci o ukupnom broju učitanih 
# brojeva iz zadanog raspona, koliko je parnih a koliko neparnih, suma parnih i suma neparnih 
# i koliko je bilo unosa brojeva izvan zadanog raspona.

_loop = True

parniSuma = 0
parniCount = 0
neparniSuma = 0
neparniCount = 0
uRasponuCount = 0
vanRasponaCount = 0

while _loop:
    unosBroj = int(input("Unesi cijeli broj izmedu 1 i 100: "))

    if(unosBroj >= 1 and unosBroj <= 100):
        if(unosBroj % 2 == 0):
            parniSuma += unosBroj
            parniCount += 1
        else:
            neparniSuma += unosBroj
            neparniCount += 1
        uRasponuCount += 1
    else:
        vanRasponaCount += 1
        print("Upisani broj nije u radanom rasponu!")

    if(parniSuma > 100 and neparniSuma > 100):
        print(F"Ukupan broj unosa u rasponu: {uRasponuCount}")
        print(F"Ukupan broj unosa van raspona: {vanRasponaCount}")
        print(F"Broj parnih: {parniCount}, Suma parnih: {parniSuma}")
        print(F"Broj parnih: {neparniCount}, Suma parnih: {neparniSuma}")

        _loop = False