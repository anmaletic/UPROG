# Napišite program koji će ispisati sve djelitelje unesenog prirodnog broja te koliko ih ima. Ukoliko 
# uneseni broj nije prirodni, unos se ponavlja (while petlja). Kada se učita prirodni broj, izlazi se iz 
# petlje i pronalaze djelitelji tog broja.
# Za traženje,ispis i prebrojavanje djelitelja koristite for strukturu ponavljanja.

broj = { "Unos" : 0, "Djelitelji" : 0, "Count" : 0}

while True:
    broj["Unos"] = int(input("Unesite prirodni broj: "))

    if(broj["Unos"] >= 1):
        break

broj["Djelitelji"] = []

for i in range(1, broj["Unos"] + 1):
    if(broj["Unos"] % i == 0):
        broj["Djelitelji"].append(i)   

broj["Count"] = len(broj["Djelitelji"])
                
print("Djelitelji broja {} su {}".format(broj["Unos"], str(broj["Djelitelji"])[1:-1]) )

print("Broj {} ima {} djelitelja.".format(broj["Unos"], broj["Count"]))
