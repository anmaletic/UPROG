# Zadatak 3
# Pomoću funkcije list kreirajte listu koja će se sastojati od brojeva iz intervala od 10 do n. Ispišite je. 
# Koristeći konprehenziju kreirajte novu listu koja će iz prethodne liste uzimati samo one brojeve koji su čitano 
# s lijeva na desno i s desna na lijevo jednaki. Ispišite koliko je brojeva zadovoljilo uvjet.

title = "Lista brojeva od 10 do n"
print(title)
print("_" * len(title))

unosN = int(input("n = "))

listaBrojeva = list(range(10, unosN+1))
print(listaBrojeva)

listaIstih = list(num for num in listaBrojeva if str(num) == str(num)[::-1])
print(listaIstih)