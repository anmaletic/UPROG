# Napišite program koji će ispisati koliko samoglasnika ima u nekom unesenom tekstu. U 
# funkciji main je unos teksta i ispis rezultata. Funkcija broji_sam (ima jedan parametar) vraća 
# broj samoglasnika u tekstu. Koristite operator in.

def broji_sam(tekst):
    count = 0
    for slovo in tekst:
        if slovo in "aeiou":
            count += 1
    return count

def main():
    unosTekst = input("Unesite tekst: ")
    print(F"U unesenom tekstu ima {broji_sam(unosTekst.lower())} samoglasnika.")

main()