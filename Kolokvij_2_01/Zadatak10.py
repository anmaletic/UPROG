# Napišite program koji će unositi jednu rečenicu i promijeniti je na način da se svako 
# pojavljivanje znakovnog niza 'ije' ili 'je' zamijeni sa znakom '?' . Potom se ta nova rečenica 
# ispisuje.


unosTekst = input("Unesite tekst: ")

index = unosTekst.find('ije')
if(index > 0):
    tempTekst = unosTekst.replace('ije', '?')

index = tempTekst.find('je')
if(index > 0):
    resTekst = tempTekst.replace('je', '?')

print(resTekst)