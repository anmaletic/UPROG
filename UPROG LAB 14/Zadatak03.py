# Zadatak 3
# Imate dva mobitela i bilježite potrošnju za 6 mjeseci u dvije liste. Te se potrošnje tabelarno ispisuju. Nakon
# toga se porede potrošnje prvog i drugog mobitela po pojedinačnim mjesecima – u prvoj listi će biti manji od
# tih iznosa, u drugoj veći. Te se potrošnje tabelarno ispisuju.
# Program se sastoji od tri funkcije: main(), ispis(), minmax(). U glavnoj funkciji je stvaranje dvije liste za
# potrošnju po mjesecima. Funkcija minmax() prima te dvije liste i mijenja njihove vrijednosti ovisno o rezultatu
# poredbe (u prvu listu ide manja od potrošnji u tom mjesecu).
# Funkcija ispis() ispisuje tabelarno te dvije liste prije i nakon poziva minmax() funkcije

def ispis(l1, l2):
    print()
    print("Mjesec:         0     1     2     3     4     5")

    print("Potrošnja1:  ", end = "")
    for item in l1:
        print("{:>4}".format(item), end="  ")        
    print()

    print("Potrošnja2:  ", end = "")
    for item in l2:
        print("{:>4}".format(item), end="  ")
    print()
    

def minmax(l1, l2):
    for i in range(6):
        if l1[i] > l2[i]:
            l1[i], l2[i] = l2[i], l1[i]

def main():
    list1 = [123, 45, 145, 8, 16, 34]
    list2 = [45, 67, 124, 13, 23, 98]

    ispis(list1, list2)
    minmax(list1, list2)
    ispis(list1, list2)

main()