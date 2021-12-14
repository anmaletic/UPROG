# Zadatak 2
# Napišite program za unos n brojeva u listu. Nakon unosa ispišite elemente liste. Zatim listu sortirajte i 
# ponovno ispišite. Uklonite sva ponavljanja brojeva i ispišite listu i podatak koliko je brojeva uklonjeno.

unosN = int(input("Unesite broj elemenata: "))

listaBrojeva = list(int(input(F"Unesite {i+1}. broj: ")) for i in range (unosN))

print(F"Pocetna lista: {listaBrojeva}")

listaBrojeva.sort()

print(F"Sortirana lista: {listaBrojeva}")

i = 0
count = 0

while i < len(listaBrojeva):    
    if i == len(listaBrojeva) - 1:
            break

    if(listaBrojeva[i] == listaBrojeva[i+1]):
        listaBrojeva.pop(i+1)
        count = count + 1
    else:
        i = i + 1       

print(F"Lista bez ponavljanja: {listaBrojeva}")
print(F"Broj pobrisanih brojeva: {count}")

