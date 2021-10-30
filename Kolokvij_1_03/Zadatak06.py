# Napišite program za unos cijene nekog proizvoda. Ako je cijena veća od 250 kn napišite 
# 'skupo', ako je < 30 kn napišite 'jeftino', inače napišite 'kupujem'.

unosCijena = float(input("Unesite cijenu proizvoda: "))


if(unosCijena > 250):
    print("Skupo")
elif(unosCijena < 30):
    print("Jeftino")
else:
    print("Kupujem")