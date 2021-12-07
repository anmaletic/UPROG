# Zadatak 4 – kreiranje liste
# Uđite u Python Shell i unesite dolje prikazane naredbe. Jesu li Vam jasne i naredbe i rezultati njihovog 
# izvršenja? Ispravite grešku u prvoj for petlji, tako da se elementi liste ispisuje preko indeksa.

lista_samoglasnika = [ 'a', 'e', 'i', 'o', 'u' ]

print(lista_samoglasnika)

len(lista_samoglasnika)

lista_samoglasnika[0]

lista_samoglasnika[:3]

lista_samoglasnika[3:]

lista_samoglasnika[3:4]

for i in range(len(lista_samoglasnika)):
    print(lista_samoglasnika[i], end = ", ")

for samoglasnik in lista_samoglasnika:
    print(samoglasnik, end = ", ")


L_br = list(range(20))
L_br
L_br = list(range(2, 20, 2))
L_br
L_zn = list("Python")
L_zn
len(L_zn)
L_zn[1]
