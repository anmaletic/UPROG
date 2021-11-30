# Zadatak 7
# Napisati program koji će unositi jednu rečenicu i na osnovu zadnjeg znaka rečenice ('.', '?', '!') 
# ispisati da li je rečenica izjavna, upitna ili usklična. Potom ispisati koliko riječi ima rečenica, te 
# ispisati pojedinačne riječi jednu ispod druge. 
# Ako rečenica ne završava niti jednim od tih znakova napisati odgovarajuću poruku i završiti 
# program.

unosTekst = input("Unesite neku recenicu: ")

zadnjiZnak = unosTekst[-1]

if zadnjiZnak == "?":
    print("Recenica je upitna")
elif zadnjiZnak == ".":
    print("Recenica je izjavna")
elif zadnjiZnak == "!":
    print("Recenica je usklicna")
else:
    print("Recenica ne zavrsava znakom '.', '?' ili '!'.")

rijec = unosTekst.split(" ")

print(F"Recenica ima {len(rijec)} rijeci.")

for item in rijec:
    print(item)
