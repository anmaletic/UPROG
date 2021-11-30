# Zadatak 4
# Napišite program koji broji koliko se puta uneseni znak pojavljuje u unesenom nizu znakova.
# U funkciji main je unos stringa i unos znaka. Vrijednosti tih dviju varijabli predaju se funkciji 
# brojiZnak koja pozivnom kodu vraća podatak koliko se puta uneseni znak pojavljuje u stringu.
# Ponavljajte unos i poziv funkcije sve dok korisnik ne unese prazan string u bilo koju od 
# varijabli.
# Zadatak prvo riješite pomoću metode count, potom bez metode count.


def brojiZnak(string, znak):
    count = 0
    for i in string:
        if i == znak:
            count += 1    
    return count

def brojiZnakCount(string, znak):
    return string.count(znak)


def main():
    while True:
        unosString = input("Unesite tekst: ")
        unosZnak = input("Unesite znak: ")

        if unosString == "" or unosZnak == "":
            break

        print(F"Znak {unosZnak} ponavlja se {brojiZnak(unosString, unosZnak)} puta.")
        print(F"Znak {unosZnak} ponavlja se {brojiZnakCount(unosString, unosZnak)} puta.")


main()