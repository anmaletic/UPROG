# Napišite program koji računa najveći zajednički djelitelj (NZD) dvaju prirodnih brojeva (nemojte 
# koristiti built – in funkciju gcd). 
# U glavnoj (main) funkciji korisnik unosi oba broja. Omogućite ponavljanje izvođenja programa 
# sve dok su uneseni brojevi veći od nule.
# Napišite funkciju koja prihvaća dva prirodna broja te vraća njihov najveći zajednički djelitelj. 
# Najveći zajednički djelitelj dvaju prirodnih brojeva je najveći prirodni broj s kojim su oba broja 
# dijeljiva bez ostatka. 
# Pri traženju NZD krenite od manjeg broja.
# Ako su npr. uneseni brojevi 35 i 7 krenut ćemo od broja 7. broj 7 dijeli bez ostatka i 7 i 35 i on je 
# NZD. Ako npr. unesemo brojeve 35 i 15 onda 15 ne dijeli oba broja bez ostatka pa provjeravate 
# 14, 13….dok ne dođete do prvog broja koji dijeli i 15 i 35. Taj broj je traženi NZD. U našem slučaju 
# to je broj 5. 

def GetDjelitelj(p_br1, p_br2):
    '''Pronalazi najveći zajednički djelitelj dva broja.'''
    loopRange = p_br1
    if (p_br1 > p_br2):
        loopRange = p_br2

    for i in range(loopRange, 0, -1):
        if(p_br1 % i == 0 and p_br2 % i == 0):
             return i
        

def main():
    title = "NAJVEĆI ZAJEDNIČKI DJELITELJ DVA BROJA"
    print(title)
    print("-" * len(title))

    print("n <= 0 za KRAJ")

    while True:
        print()
        unosBr1 = int(input("Unesite prvi broj  : "))
        unosBr2 = int(input("Unesite drugi broj : "))
    
        if(unosBr1 <= 0 or unosBr2 <= 0):
            break
        else:
            print(F"Najveći zajednički djelitelj brojeva {unosBr1} i {unosBr2} je {GetDjelitelj(unosBr1, unosBr2)}")
            print()


main()