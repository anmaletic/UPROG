#   U semestru imate pet predmeta označenih brojevima od 1 do 5. Iz jednog predmeta ocjena nije 
#   zaključena i redni broj tog predmeta se ne unosi. Program na kraju ispisuje redni broj predmeta za 
#   koji nije zaključena ocjena. Podrazumijeva se da su brojevi ispravno uneseni.

#predmeti = [ 1, 2, 3, 4, 5]

predmeti = []

for i in range(5):
    predmeti.append(i+1)

for i in range(4):
 
    unos = int(input("Unesite redni broj predmeta: "))
    predmeti.remove(unos)

#print("Preostali predmet je: ", str(predmeti)[1:-1]) 
print("Preostali predmet je: ", predmeti[0]) 
