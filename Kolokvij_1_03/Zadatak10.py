# Program učitava osvojene bodove iz ispita za n studenata. Ispisuju se najveći i najmanji bodovi, te 
# prosijek bodova. Koristite for petlju . Podrazumijeva se da je korisnik unosio bodove iz raspona 0 –
# 100.

ukupniBodovi = 0

unosBrojStudenata = int(input("Unesite broj studenata: "))

for i in range(unosBrojStudenata):
    unosBodovi = float(input(F"Unesite bodove {i+1}. studenta: "))

    if(i == 0):
        minBodovi = unosBodovi
        maxBodovi = unosBodovi
    elif(minBodovi > unosBodovi):
        minBodovi = unosBodovi
    elif(maxBodovi < unosBodovi):
        maxBodovi = unosBodovi

    ukupniBodovi += unosBodovi

prosjekBodovi = ukupniBodovi / unosBrojStudenata

print(F"Najmanji bodovi: {minBodovi}")
print(F"Najveci bodovi: {maxBodovi}")
print(F"Prosjek bodova: {prosjekBodovi}")
