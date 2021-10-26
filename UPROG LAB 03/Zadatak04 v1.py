# Kupit ćete košulju samo ako cijena nije veća od 100kn, broj je 42 i boja je bijela ili zelena. Nakon unesenih 
# vrijednosti ispisuje se poruka ''Kupujem'' ako su svi uvjeti zadovoljeni, u suprotnom se ispisuje poruka ''Ne 
# kupujem''. Napišite složeni uvjet koristeći logičke operatore and i or.
# Obavezno provjerite radi li složeni logički uvjet dobro na sve kombinacije istinitosti relacijskih izraza.

class Kosulja:
    def __init__(self, Cijena, Broj, Boja):
        self.Cijena = Cijena
        self.Broj = Broj
        self.Boja = Boja
    
def Kontrola(unos):

    if(unos.Cijena <= 100 and 
       unos.Broj == 42 and 
       (unos.Boja == "bijela" or unos.Boja == "zelena")):

        return "Kupujem"
    else:
        return "Ne kupujem"

    
unosKosulja = Kosulja(0, 0, 0)

unosKosulja.Cijena = float(input("Unesite cijenu: "))
unosKosulja.Broj = int(input("Unesite broj: "))
unosKosulja.Boja = input("Unesite boju: ")

result = Kontrola(unosKosulja)

print(result)