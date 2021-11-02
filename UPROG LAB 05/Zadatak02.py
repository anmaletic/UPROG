# Napišite program koji učitava prirodan broj te pronalazi i ispisuje najveću znamenku toga 
# broja. 
# Ponavljanje provjere pojedine znamenke broja se prekida kada su sve znamenke obrađenje 
# ili se pojavila znamenka 9 pa nema smisla dalje tražiti najveću znamenku. Koristite while
# petlja i naredbu break.


while True:
    unosBroj = int(input("Unesite cijeli broj: "))

    maxNum = 0
    for temp_num in str(unosBroj):
        num = int(temp_num)
        if(num == 9):
            maxNum = num
            break
        else:
            if(maxNum < num):
                maxNum = num
    break

print(F"Najveca znamenka broja {unosBroj} je {maxNum}.")
