# Napišite program za ispis svih savršenih brojeva iz nekog intervala od 2 do n.
# Broj je savršen ako je jednak sumi svojih pozitivnih djelitelja manjih od njega.
# Npr. 6 i 28 su savršeni brojevi:
# 6 = 1+2+3
# 28 = 1+2+4+7+14.
# Definirajte dvije funkcije, savrsen_broj i main. U funkciji main učitava se gornja granica intervala i poziva
# se funkcija savrsen_broj. Funkcija savrsen_broj traži i ispisuje savršene brojeve.
# Upute za rad:
#    Podrazumijeva se da je korisnik za gornju granicu intervala unio prirodan broj.
#    Unutar funkcije savrsen_broj u brojaču vanjske for petlje generirajte brojeve od 2 do gornje granice
#    U unutarnjoj petlji za svaki broj iz zadanog raspona tražite djelitelje manje od njega. Dovoljno je tražiti
#       ih od 1 do polovine broja.
#    U glavnom programu pozovite funkciju main.

def savrsen_broj(a):
    '''Provjerava dali je broj savrsen te ispisuje rezultat.'''

    for i in range(2, a):
        sum_djelitelja = 0
        for j in range(1, i // 2 + 1):
            if(i % j == 0):
                sum_djelitelja += j

        if(i == sum_djelitelja):
    	     print(F"{i}")
     
def main():
    title = "SAVRSENI BROJEVI"
    print(title)
    print("_" * len(title))
    print()

    unos = int(input("Unesite gornju granicu intervala: "))
    print()

    title = F"Savrseni brojevi iz intervala 2 - {unos}"
    print(title)
    print("*" * len(title))
    print()

    savrsen_broj(unos)

main()
