#   Napišite program koji od korisnika traži unos dva broja. Brojevi se potom ispisuju. Zatim se vrijednosti 
#   varijabli zamjenjuju, te se ponovo ispisuju (istim redoslijedom varijabli). Zadatak riješite na tri načina:
#   a) uvođenjem pomoćne varijable
#   b) naredbom višestrukog pridruživanja
#   c) korištenjem suprotnih aritmetičkih operatora (+ i - ili * i /)

unosBroj1 = float(input("Unesite prvi broj: "))
unosBroj2 = float(input("Unesite drugi broj: "))

x = unosBroj1
y = unosBroj2

print("")
print("Prije zamjene vrijednosti")
print("-" * 30)

print(F"x = {x}     y = {y}")

print("Nakon zamjene vrijednosti")
print("")
print("-" * 30)

print("a) Uvođenjem pomoćne varijable")

temp = x        # temp kao pomocna varijabla
x = y
y = temp

print(F"x = {x}     y = {y}")
print("")

print("b) Naredbom višestrukog pridruživanja")

x, y = y, x     # visestruko pridruzivanje

print(F"x = {x}     y = {y}")
print("")

print("c) Korištenjem suprotnih aritmetičkih operatora")

x = x + y       # koristenje suprotnih aritmetickih operatora + i -
y = x - y
x = x - y

print(F"x = {x}     y = {y}")
print("")

x = x * y       # koristenje suprotnih aritmetickih operatora * i /
y = x / y
x = x / y

print(F"x = {x}     y = {y}")
print("")