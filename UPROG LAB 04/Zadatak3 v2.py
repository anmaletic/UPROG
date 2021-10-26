# Omogućiti korisniku unos 5 troznamenkastih brojeva. Za svaki uneseni broj izračunava se i 
# ispisuje umnožak njegovih znamenki. Koristite for petlju. Po izlasku iz petlje ispisuje se zbroj svih 
# umnožaka.
# Podrazumijeva se da je korisnik unio troznamenkast broj. 

zbroj = 0

for i in range(5):
    unosBroj = int(input(F"Unesite {i+1}. broj: "))
    
    prvaZnamenka = unosBroj // 100
    drugaZnamenka = unosBroj % 100 // 10
    trecaZnamenka = unosBroj % 10

    umnozak = prvaZnamenka * drugaZnamenka * trecaZnamenka

    zbroj += umnozak

    print(F"{prvaZnamenka} * {drugaZnamenka} * {trecaZnamenka} = {umnozak}")

print(F"Zbroj umnozaka je {zbroj}.")