# 5.
# Napišite program koji stvara liste cijelih brojeva L1 i L2. Prvu listu stvorite nabrajanjem 
# elemenata. Drugoj listi for petljom i metodom append dodajte n cijelih brojeva. Zatim se 
# komprehenzijom kreira nova lista Lpresjek čiji su elementi samo oni brojevi koji se nalaze 
# i u L1 i u L2. Npr., ako je L1 = [20, 18, 4, 5] i L2 = [6, 4, 70, -3, 5], Lprsjek će biti [4, 5].
# Ispišite sve tri liste.

def main():
    L1 = [ 5, 94, 12, 65, 23, 10, 32, 54 ]

    unosCount = int(input("Koliko ce brojeva biti u listi? "))
    L2 = [int(input(F"{i+1}. broj: ")) for i in range(unosCount)]

    Lpresjek = [num for num in L2 if num in L1]

    print(L1)
    print(L2)
    print(Lpresjek)

main()