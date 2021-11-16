# U glavnom programu (izvan funkcija) pridružite varijabli x vrijednost 5 i ispišite njenu vrijednost.
# Definirajte dvije bezparametarske funkcije ispis1 i ispis2 i u obje jednostavno ispišite vrijednost
# varijable x. Pozovite obje funkcije, prvi ispis1, pa ispis2. Kakav je ispis i zašto?
# Sada u funkciji ispis1 promijenite vrijednost varijable x, uvećajte je za 1. Pokrenite program. Koju
# grešku javlja interpreter?
# Sada u funkciji ispis1 kao prvu liniju koda napišite global x. Pokrenite program. Kakav je ispis sada
# i zašto?
# Zašto je ispravnije umjesto globalne varijable imati lokalnu varijablu koja se po potrebi
# prosljeđuje procedurama?
# Sada umjesto global x napišite x=1. Kakav je ispis sada i zašto?
# Neka sada funkcija ispis1 ima jedan parametar, nazovimo ga x i pozovite funkciju na argumentu x.
# Kakav je ispis sada i zašto?
# Je li promjena pripadajućeg parametra utjecala na pripadajući argument?


def ispis1(x):
    #global x              # koristi se globalna varijabla
    #x = 1                 # lokalna varijabla 
    x = x + 1              # local variable 'x' referenced before assignment, x nije definiran
    print(x)

def ispis2():
    print(x)



x = 5

print(x)
ispis1(x)
ispis2()