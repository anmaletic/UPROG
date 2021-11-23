# Napišite program za računanje prosječne vrijednosti izlaznih rezultata kolokvija. U glavnoj funkciji
# korisnik upisuje koliko je studenata izašlo na kolokvij. Taj podatak se šalje funkciji koja obavi 
# unos bodova (0-100) za svakog studenta, izračuna sumu i vrati prosječnu vrijednost bodova. U 
# glavnoj funkciji se ispisuje poruka ovisno o vraćenom prosjeku. Ako je prosjek veći od 60 ispisuje 
# se poruka „Zadovoljavajući rezultati“, ako je između 40 i 60 ispisuje se poruka „Dobri rezultati“, u 
# suprotnom se ispisuje poruka „Moglo je i bolje“. 
# Koristite if…else strukturu odluke i for petlju.

def UnosBodova(brojStud):
    '''Unos bodova svakog studenta. Vraća prosjek.'''
    sum = 0
    for i in range(1, brojStud + 1):
        unosBod = int(input(F"Unesite broj bodova {i}. studenta (0-100): "))
        sum += unosBod
    return round(sum / brojStud, 2)

def main():
    unosBrojStudenata = int(input("Unesi koliko je studenata izašlo na kolokvij: "))

    prosjek = UnosBodova(unosBrojStudenata)
    if prosjek > 60:
        print(F"Zadovoljavajući rezultati. ({prosjek})")
    elif prosjek > 40:
        print(F"Dobri rezultati. ({prosjek})")
    else:
        print(F"Moglo je i bolje. ({prosjek})")

main()