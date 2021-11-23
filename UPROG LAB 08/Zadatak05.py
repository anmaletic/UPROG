# Napišite program koji na osnovu x i y koordinata točke ( u mm) ispisuje u kojem se kvadrantu 
# točka nalazi i koliko je udaljena od ishodišta. Unos koordinata je u glavnoj funkciji. Te se 
# koordinate prosljeđuju funkciji koja ispisuje u kojem je kvadrantu ta točka i koliko je udaljena od 
# ishodišta. Ponavljajte unos koordinata i poziv funkcije sve dok su obje koordinate različite od 
# nule. 
# Ispis treba izgledati ovako: npr. „točka t(4,-6) je u četvrtom kvadrantu. Od ishodišta je udaljena 
# 7.21 mm“.

import math

def KontrolaUnosa(x, y):
    '''Ispisuje u kojem kvadrantu se točka nalazi i udaljenost od ishodišta.'''
    if x > 0 and y > 0:
        kvadrant = 1
    elif x < 0 and y > 0:
        kvadrant = 2
    elif x < 0 and y < 0:
        kvadrant = 3
    else:
        kvadrant = 4

    udaljenost = math.sqrt(x**2 + y**2)

    print(F"Točka sa koordinatama ({x},{y}) nalazi se u {kvadrant}. kvadrantu.")
    print(F"Od ishodišta je udaljena {round(udaljenost, 2)} mm.")
    
def main():
    while True:
        print("-" * 60)
        unosX = int(input("Unesite x: "))
        unosY = int(input("Unesite y: "))
        print()

        if(unosX == 0 or unosY == 0):
            break

        KontrolaUnosa(unosX, unosY)

main()