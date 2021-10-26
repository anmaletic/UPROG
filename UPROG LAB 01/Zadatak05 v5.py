#   U semestru imate pet predmeta označenih brojevima od 1 do 5. Iz jednog predmeta ocjena nije 
#   zaključena i redni broj tog predmeta se ne unosi. Program na kraju ispisuje redni broj predmeta za 
#   koji nije zaključena ocjena. Podrazumijeva se da su brojevi ispravno uneseni.

p1 = int(input("Unesite redni broj predmeta: "))
p2 = int(input("Unesite redni broj predmeta: "))
p3 = int(input("Unesite redni broj predmeta: "))
p4 = int(input("Unesite redni broj predmeta: "))

p5 = 15 - p1 - p2 -p3 - p4

print("Preostali predmet je:", p5)