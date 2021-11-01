#   Napišite program koji na osnovu učitane godine g ispisuje naziv povijesnog razdoblja . Koristite 
#   if…..elif….else naredbu grananja.

#   Godina          Razdoblje
#   g < -3500       Prapovijest
#   -3500 ≤ g <0    Povijest
#   0 ≤ g < 476     Stari vijek
#   476 ≤ g <1492   Srednji vijek

unosGodina = int(input("Unesite godinu: "))

if(unosGodina <-3500):
    print("Prapovijest")
elif(unosGodina >= -3500 and unosGodina < 0):
    print("Povijest")
elif(unosGodina >= 0 and unosGodina < 476):
    print("Stari vijek")
else:
    print("Srednji vijek")