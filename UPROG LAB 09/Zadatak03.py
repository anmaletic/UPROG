# Zadatak 3 - dohvat znaka preko indeksa, ugrađena metoda find, operator
#             konkatenacije(spajanja stringova) '+'
# Napisati program za unos imena i prezimena osobe (kao jedan string). Ispisati inicijale. 
# Ponavljati unos i ispis sve dok korisnik ne unese prazan string.
# Podrazumijeva se da je između imena i prezimena samo jedna razmaknica i da je to jedina 
# razmaknica u unosu. Zadatak riješite pomoću metode find i dohvata znaka preko indeksa.


while True:
    unosImePrezime = input("Unesite ime i prezime: ")

    if unosImePrezime == "":
        break

    razmak = unosImePrezime.find(" ")
    print(F"{unosImePrezime[0]}. {unosImePrezime[razmak + 1]}.")
