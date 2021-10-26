# Napišite program koji će ispisati poruku ovisno o unesenom cijelom broju. Koristite 
# if…..elif….else naredbu grananja. Nemojte koristiti logičke operatore.

unosBroj = int(input("Unesite broj: "))

if(unosBroj < 0):
    print("Negativan broj.")
elif(unosBroj <= 9):
    print("Jednoznamenkast")
elif(unosBroj <= 99):
    print("Dvoznamenkast")
elif(unosBroj <= 999):
    print("Troznamenkast")
else:
    print("Izvan raspona")