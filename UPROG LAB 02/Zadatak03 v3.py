#   Napišite program koji će tražiti od korisnika unos realnog broja x te ispisati vrijednost varijable f: 
#
#          x, x > 0
#   f = { −x, x < 0
#          0, x = 0

unos = float(input("Unesite jedan broj: "))

if(unos >= 0):
    f = unos
else:
    f = -unos

print(F"{f}")