# Napisati program koji omogućuje korisniku da unese tri cjelobrojne vrijednosti u varijable a, b, i c. Njihove 
# vrijednosti se ispisuju. Nakon obrade u varijabli a treba biti najmanji od ta tri broja, u varijabli b srednji, a u 
# varijabli c najveći. Njihove vrijednosti se ponovno ispisuju.
# Zadatak riješite pomoću tri if naredbe i tri naredbe višestrukog pridrživanja (sjetite se zamijene vrijednosti 
# dviju varijabli iz vježbe 2).

title = "Unesite tri nejednaka cijela broja"
print(title)
print("-" * len(title))

unosA = int(input("a = "))
unosB = int(input("b = "))
unosC = int(input("c = "))

if(unosA != unosB and unosB != unosC and unosA != unosC):
    print(F"a = {unosA}, b = {unosB}, c = {unosC}")

    if(unosA > unosB):
        unosA, unosB = unosB, unosA
    if(unosB > unosC):
        unosB, unosC = unosC, unosB
    if(unosA > unosB):
        unosA, unosB = unosB, unosA

    print(F"a = {unosA}, b = {unosB}, c = {unosC}")

else:
    print("Brojevi nisu nejednaki.")