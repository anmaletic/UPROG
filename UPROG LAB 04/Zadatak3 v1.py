# Omogućiti korisniku unos 5 troznamenkastih brojeva. Za svaki uneseni broj izračunava se i 
# ispisuje umnožak njegovih znamenki. Koristite for petlju. Po izlasku iz petlje ispisuje se zbroj svih 
# umnožaka.
# Podrazumijeva se da je korisnik unio troznamenkast broj. 

def GetZnamenke(broj):
    prvaZnamenka = broj // 100
    drugaZnamenka = broj % 100 // 10
    trecaZnamenka = broj % 10

    umnozak = prvaZnamenka * drugaZnamenka * trecaZnamenka

    return prvaZnamenka, drugaZnamenka, trecaZnamenka, umnozak

zbroj = 0

for i in range(5):
    unosBroj = int(input(F"Unesite {i+1}. broj: "))
    result = GetZnamenke(unosBroj)

    zbroj += result[3]

    print(F"{result[0]} * {result[1]} * {result[2]} = {result[3]}")

print(F"Zbroj umnozaka je {zbroj}.")