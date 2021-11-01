# Korisnik unosi cijeli broj. Ako je broj prirodan računa se i ispisuje zbroj znamenki unesenog 
# broja, u suprotnom se ispisuje poruka 'uneseni broj nije prirodan'

while True:
    unosBroj = int(input("Unesite cijeli broj: "))
    if(unosBroj < 1):
        print("Uneseni broj nije prirodan.")
    else:
        zbrojZnam = 0
        for num in str(unosBroj):
            zbrojZnam += int(num)

        print(F"Zbroj znamenki broja {unosBroj} je {zbrojZnam}.")