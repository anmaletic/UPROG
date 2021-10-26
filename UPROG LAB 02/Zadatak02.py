#   Napišite program koji od korisnika traži unos dva cijela broja. Ako je prvi broj djeljiv drugim brojem 
#   ispisuje se poruka „a je djeljivo sa b“, u suprotnom se ispisuje poruka „a nije djeljivo sa b“, pri tome 
#   umjesto a i b treba ispisati unesene brojeve (npr. 22 nije djeljivo sa 3)

unosBroj1 = int(input("Unesi prvi (cijeli) broj: "))
unosBroj2 = int(input("Unesi drugi (cijeli) broj: "))

if(unosBroj1 % unosBroj2 == 0):
    print(F"{unosBroj1} je djeljivo sa {unosBroj2}")
else:    
    print(F"{unosBroj1} nije djeljivo sa {unosBroj2}")