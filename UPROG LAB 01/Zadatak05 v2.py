#   U semestru imate pet predmeta označenih brojevima od 1 do 5. Iz jednog predmeta ocjena nije 
#   zaključena i redni broj tog predmeta se ne unosi. Program na kraju ispisuje redni broj predmeta za 
#   koji nije zaključena ocjena. Podrazumijeva se da su brojevi ispravno uneseni.

p = 10

for i in range(p-1):
    p += i + 1 
    unos = int(input("Unesite redni broj predmeta: "))
    p -= unos

print("Preostali predmet je: ", p) 

