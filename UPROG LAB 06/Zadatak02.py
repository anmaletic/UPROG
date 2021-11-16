# Zadatak 2 – funkcija koja vraća vrijednost, naredba return

# Prethodni zadatak sada riješite pomoću dvije funkcije - povrsina_pravokutnika koja vraća 
# površinu i dijagonala_pravokutnika koja vraća dijagonalu. 
# Povratne vrijednosti pohranite u varijable, pa ih potom ispišite. 
# Promijenite kod tako da zakomentirate naredbe u kojima su varijablama pridružene 
# vrijednosti tih funkcija i pozovite funkcije unutar naredbe print.

from math import sqrt

def povrsina_pravokutnika(p_unosA, p_unosB):
    povrsina = p_unosA * p_unosB
    return povrsina

def dijagonala_pravokutnika(p_unosA, p_unosB):
    dijagonala = round(sqrt(p_unosA**2 + p_unosB**2), 2)
    return dijagonala

while True:
    unosA = float(input("stranica a = "))
    unosB = float(input("stranica b = "))

    if(unosA <= 0 or unosB <= 0):
        break

    pov = povrsina_pravokutnika(unosA, unosB)
    print(F"P = {pov}")

    dij = dijagonala_pravokutnika(unosA, unosB)
    print(F"d = {dij}")

    # print(F"P = {povrsina_pravokutnika(unosA, unosB)}")
    # print(F"d = {dijagonala_pravokutnika(unosA, unosB)}")