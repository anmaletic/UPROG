# Ispišite prvu i zadnju znamenku unesenog troznamenkastog broja. Koristite funkciju 
# divmod. Ukoliko broj nije troznamenkati, ispisuje se poruka o tome i program završava

unos = int(input("Unesite troznamenkasti broj: "))

if(unos // 100 == 0 or unos // 100 >= 10):
    print("Uneseni broj nije troznamenkasti!")

else:
    if(unos < 0):
        unos = -unos                        # % za negativni broj radi cudno :)

    prvaZnamenka = divmod(unos, 100)[0]     # divmod vraca (x, y) -> [0] znaci da zelimo vrijednost x-a
    zadnjaZnamenka = divmod(unos, 10)[1]    # divmod vraca (x, y) -> [1] znaci da zelimo vrijednost y-a


    print(F"Prva znamenka je {prvaZnamenka}, a zadnja {zadnjaZnamenka}.")