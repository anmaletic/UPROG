# Napišite program koji će ispisati sve djelitelje unesenog pozitivnog cijelog broja te koliko ih 
# ima. Podrazumijeva se da je korisnik unio pozitivni cijeli broj broj. Koristite for petlju.

unos = int(input("Unesite pozitivni cijeli broj: "))

djelitelji = []

for i in range(unos):
    if(unos % (i+1) == 0):
        djelitelji.append(i+1)

# print(F"{unos} ima {len(djelitelji)} i to su: {*djelitelji}")     # *(unpack)  ne radi u F"{}"

print(F"{unos} ima {len(djelitelji)} djelitelja i to su: {str(djelitelji)[1:-1]}") 