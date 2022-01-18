# Zadatak 4
# # Napišite program koji će unositi jedan izraz koji ima neke od operatora +, -, *, **, %, / i //. Prije i poslije
# operatora nema razmaka. Ispravite zapis na način da se prije i poslije svakog operatora doda razmaknica.
# Potom se taj izraz ispisuje.
# Npr, ako je uneseno (x+y)**2/2*(x+y) izlaz treba biti (x + y) ** 2 / 2 * (x + y)

listOperatori = ["+", "-", "*", ",,", "%", "/", ".."]

unosIzraz = input("Unesite izraz:  ")
print(unosIzraz)

unosIzraz = unosIzraz.replace("//", "..")
unosIzraz = unosIzraz.replace("**", ",,")

for op in listOperatori:
    if op in unosIzraz:
        unosIzraz = unosIzraz.replace(op, F" {op} ")

unosIzraz = unosIzraz.replace("..", "//")
unosIzraz = unosIzraz.replace(",,", "**")

print(unosIzraz)