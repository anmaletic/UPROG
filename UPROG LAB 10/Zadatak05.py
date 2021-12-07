# Zadatak 5
# Napišite program za unos 10 brojeva u listu. Brojevi se unose u for petlji preko indeksa. Naravno, prije 
# petlje stvorite listu i sve članove inicijalizirajte na 0 (ime_liste = [0] *10). Potom ispišite sve brojeve, 
# njihov zbroj i najveći i najmanji broj. Koristiti funkcije sum, min i max (min(ime_liste)).
# Promijenite sada kod tako da u for petlji koristite funkciju append.

listaBR = [0] * 10

def main():
    for i in range(len(listaBR)):
        listaBR[i] = int(input(F"Unesite {i+1}. broj: "))

    print(*listaBR)
    print(sum(listaBR))
    print(min(listaBR))
    print(max(listaBR))

main()