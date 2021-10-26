# Napišite program koji traži od korisnika unos dvoznamenkastog broja. Unos se ponavlja 
# ukoliko broj nije dvoznamenkast. Potom se ispisuju prva i zadnja znamenka unesenog broja, 
# te njihov zbroj. Koristite while petlju, naredbu break i funkciju divmod()

_loop = True

while _loop:
    unosBroj = int(input("Unesite dvoznamenkasti broj: "))
    
    if(unosBroj // 10 < 10):
        prvaZnamenka = divmod(unosBroj, 10)[0]
        zadnjaZnamenka = divmod(unosBroj, 10)[1]
        _loop = False
    else:
        print("Uneseni broj nije dvoznamenkasti.")

print(F"Znamenka jedinica je {zadnjaZnamenka}, a desetica {prvaZnamenka}.")
print(F"Zbroj znamenki je {prvaZnamenka + zadnjaZnamenka}.")