# Zadatak 5
# Napišite program za kreiranje liste od n imena. U glavnom programu se metodom append dodaju imena u
# listu. Elemente liste potom se ispisuju jedan ispod drugog. Zatim se lista šalje funkciji koja preslaguje elmente
# na način da imena budu poredana po broju slova - od kraćih prema dužim imenima. Tako promijenjena listu
# ponovo ispisati. 


def FillDemoData():
    return [ "Antonio", "Miroslav", "Mislav", "Petar", "Tin", "Ivan"]

def SortirajListu(lista):
    for item in lista:
        for i in range(len(lista) - 1):
            if len(lista[i]) > len(lista[i+1]):
                lista[i], lista[i+1] = lista[i+1], lista[i]

def main():
#    unosN = int(input("Broj imena: "))
#    listaImena = [input("Ime: ") for i in range(unosN)]

    listaImena = FillDemoData()
    
    print()
    for item in listaImena:
        print(item)

    SortirajListu(listaImena)

    print()
    for item in listaImena:
        print(item)   

main()