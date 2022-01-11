# Zadatak 1
# Napišite program koji će generirati listu od 30 nasumičnih cijelih brojeva od 0 do 15. Svi se brojevi iz liste 
# ispisuju. Korisnik potom unosi neki cijeli broj (od 0 do 15) te se ispisuju sve pozicije na kojima se ta vrijednost
# nalazi. 
# U funkciji main() se komprehenzijom stvara lista ( L = [randint(0, 15) ………………….]), potom se lista ispisuje, i 
# učitava se broj čije se pozicije u listi traže. 
# Funkcija lista_indexa pretražuje listu nasumičnih brojeva i vraća listu svih pozicija na kojima se nalazi uneseni 
# broj.
# U modulu random nalazi se funkcija randint(a, b) – a i b su granice intervala iz kojeg funkcija vraća jedan broj 
# svaki put kad je pozovete. 

from random import randint

def lista_indexa(listaBrojeva, broj):
    lista_ind = []
    for i in range(30):
        if(listaBrojeva[i] == broj):
            lista_ind.append(i)

    return lista_ind


def main():
    lista = list(randint(0, 15) for i in range(30))
    print(lista)

    unosBroj = int(input("Unesite broj: "))

    print(lista_indexa(lista, unosBroj))

main()