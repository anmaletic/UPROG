#   Napišite program za izračunavanje ukupnog otpora R koji daju otpornici R1 i R2 ovisno o tipu veze: 
#   korisnik bira 1 za serijski, 2 za paralelni spoj. Pri tom se podrazumijeva da je korisnik odabrao jedan 
#   od ta dva broja.

unosR1 = float(input("Unesite vrijednost otpornika R1: "))
unosR2 = float(input("Unesite vrijednost otpornika R2: "))

print("-" * 40)

print("1. Serijski spoj")
print("2. Paralelni spoj")

unosOdabir = int(input("Unesite broj odabranog spoja: "))

if(unosOdabir == 1):
    rUk = unosR1 + unosR2
    print(F"Ukupan otpor serijskog spoja je: {rUk} Ohm")
else:
    rUk = (unosR1 + unosR2) / (unosR1 * unosR2)
    print(F"Ukupan otpor paralelnog spoja je: {round(rUk, 2)} Ohm-a")

