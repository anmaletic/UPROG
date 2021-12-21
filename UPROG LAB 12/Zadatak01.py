# Zadatak 1
# Napišite program za praćenje planiranih sati učenja kroz 5 radnih dana u tjednu. Listu planirani_sati_ucenja 
# stvorite jednostavnim nabrajanjem elemenata. U listu ostvareni_sati_ucenja unesite vrijednosti for petljom. 
# Stvorite još jednu listu razlika_sati i pohranite u nju za svaki od 5 dana razliku ostvarenih i planiranih sati 
# učenja. Ispišite vrijednosti iz sve tri liste.

title = "Unos ostvarenih sati učenja"
print(title)
print("_" * len(title))

listaPlanirani = [2, 3, 5, 4, 1]
listaOstvareni = list(int(input(F"{i+1}. dan: ")) for i in range(5))

print("Planirani sati učenja")
print("_" * 25)

print(*listaPlanirani, sep="    ")
print()

print("Ostvarenih sati učenja")
print("_" * 25)

print(*listaOstvareni, sep="    ")
print()

print("Razlika")
print("_" * 25)

listaRazlika = list(listaOstvareni[i] - listaPlanirani[i] for i in range(5))

print(*listaRazlika, sep="    ")
print()