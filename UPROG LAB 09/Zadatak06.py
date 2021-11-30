# Zadatak 6 – ugrađene metode find i replace
# Napisati program koji će u unesenom tekstu zamijeniti sve znakove '+' sa znakom '*'. Ako ne 
# nađe znak '+' napisati poruku da nije nađen taj znak. 
# Ponavljati unos i obradu sve dok korisnik ne unese 'kraj'.

while True:
    unosTekst = input("Unesite tekst: ")

    if unosTekst == "kraj":
        break

    if unosTekst.find("+") > 0:
        print(unosTekst.replace("+", "*"))
    else:
        print("Nije pronaden '+'.")