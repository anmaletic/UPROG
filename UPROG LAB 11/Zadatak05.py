# Kreirajte listu čiji su elementi n-torke (naziv zemlje, glavni grad). Unesite redom: (Poljska, Varšava), (Turska, 
# Ankara), (Francuska, Pariz), (Nizozemska, Amsterdam) i (Estonija Talin). Koristeći for petlju postavite pitanje
# o glavnom gradu za svaku državu (ime države u postavljenom pitanju treba završavati na 'e'). Na kraju ispišite 
# koliko je bilo točnih odgovora.

listaDG = [("Poljska", "Varšava"), ("Turska", "Ankara"), ("Francuska", "Pariz"), ("Nizozemska", "Amsterdam"), ("Estonija", "Talin")]

print(listaDG)
i = 0
j = 1
while i < len(listaDG):
    print(F"Glavni grad {listaDG[i][0][:-1]}e je:", end = " ")
    if(listaDG[i][1] == input("")):
        print("Tocno")
        i += 1
        j = 1
    else:
        print(F"{listaDG[i][1][:j]}" + "_" * (len(listaDG[i][1]) - j))
        if(j < len(listaDG[i][1])):
            j += 1


    