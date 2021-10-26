# Želite popločati terasu dimenzija a x a pločicama pravokutnog oblika dimenzija c x d. Duljine stranica su
# prirodni brojevi. Stranice pločica izražene su u cm, a terase u m. Za unesene duljine stranica izračunajte i 
# ispišite koliko pločica biste trebali kupiti i koliko će cijelih pločica stati na terasu. Podrazumijeva se da su 
# unesene ispravne vrijednosti.
# Kad se stavi prva pločica na terasu, sve ostale se slažu na isti način

# Napomena: Kada se dio pločice izreže za popločavanje, ostatak pločice postaje neupotrebljiv

class PlociceModel:
    def __init__(self, a, b):
        self.strA = a
        self.strB = b

class TerasaModel(object):
    def __init__(self):
        self.dim = None
        self.dim_cm = None

    def SetDimension(self, value):
        self.dim = value
        self.dim_cm = value * 100

    def GetPlociceCount(self, val_1, val_2):
        
        row = self.dim_cm // val_1
        column = self.dim_cm // val_2

        plociceCount = row * column

        if(self.dim_cm % val_1 > 0):
            row = row + 1

        if(self.dim_cm % val_2 > 0):
            column = column + 1

        plociceCountTotal = row * column

        return int(plociceCount), int(plociceCountTotal)
        



plocice = PlociceModel(0,0)
terasa = TerasaModel()

title = "Dimenzije terase a*a u metrima:"
print(title)
print("-" * len(title))

terasa.SetDimension(float(input("a = ")))
print("")

title = "Dimenzije pločice c*d u centimetrima:"
print(title)
print("-" * len(title))

plocice.strA = float(input("c = "))
plocice.strB = float(input("d = "))

plociceCount = terasa.GetPlociceCount(plocice.strA, plocice.strB)

print("")
print(F"Za popločiti cijelu terasu trebate kupiti {plociceCount[1]} pločica.")
print(F"Na terasi će biti {plociceCount[0]} cijelih pločica.")