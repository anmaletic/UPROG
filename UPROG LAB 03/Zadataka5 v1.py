# Želite popločati terasu dimenzija a x a pločicama pravokutnog oblika dimenzija c x d. Duljine stranica su
# prirodni brojevi. Stranice pločica izražene su u cm, a terase u m. Za unesene duljine stranica izračunajte i 
# ispišite koliko pločica biste trebali kupiti i koliko će cijelih pločica stati na terasu. Podrazumijeva se da su 
# unesene ispravne vrijednosti.
# Kad se stavi prva pločica na terasu, sve ostale se slažu na isti način

# Napomena: Kada se dio pločice izreže za popločavanje, ostatak pločice postaje neupotrebljiv

title = "Dimenzije terase a*a u metrima:"
print(title)
print("-" * len(title))

unosTeraseA = float(input("a = "))
print("")

title = "Dimenzije pločice c*d u centimetrima:"
print(title)
print("-" * len(title))

unosPlociceC = float(input("c = "))
unosPlociceD = float(input("d = "))

dimTerasaCM = unosTeraseA * 100

plociceCountVodoravno = dimTerasaCM // unosPlociceC
plociceCountOkomito = dimTerasaCM // unosPlociceD
plociceCountCijele = plociceCountVodoravno * plociceCountOkomito

if(dimTerasaCM % unosPlociceC):
    plociceCountVodoravno = plociceCountVodoravno + 1
if(dimTerasaCM % unosPlociceD):
    plociceCountOkomito = plociceCountOkomito + 1

plociceCountTotal =  plociceCountVodoravno * plociceCountOkomito

print("")
print(F"Za popločiti cijelu terasu trebate kupiti {int(plociceCountTotal)} pločica.")
print(F"Na terasi će biti {int(plociceCountCijele)} cijelih pločica.")