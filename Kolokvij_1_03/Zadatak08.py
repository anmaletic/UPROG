# Napišite program koji će ispisati poruku ovisno o unesenom cijelom broju. Koristite 
# if…..elif….else naredbu grananja.

# broj                      poruka
# 0                         nula
# 0 < broj <= 35            loše
# 35 < broj < 40            nedovoljno
# 40 <= broj < 70           zadovoljava
# 70 <= broj <= 100         odličan
# Za ostale vrijednosti     izvan raspona

unosBroj = int(input("Unesite cijeli broj: "))

if(unosBroj >= 0 and unosBroj <= 100):
    if(unosBroj == 0):
        print("nula")
    elif(unosBroj > 0 and unosBroj <= 35):
        print("loše")
    elif(unosBroj > 35 and unosBroj < 40):
        print("nedovoljno")
    elif(unosBroj >= 40 and unosBroj < 70):
        print("zadovoljava")
    else:
        print("odlican")
else:
    print("Izvan raspona")