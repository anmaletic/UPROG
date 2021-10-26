# Napisati program za određivanje vrste trokuta na osnovu unesenih stranica. Treba prvo ispitati da li 
# stranice čine trokut, pa ako čine napisati da li je jednakostraničan, jednakokračan ili raznostraničan. Ako ne 
# čine trokut napisati odgovarajuću poruku.
# Koristiti if…elif…else strukturu odluke i logičke operatore and i or.
# Provjera stranica: zbroj duljina bilo koje dvije stranice mora biti veći od duljine treće stranice.

unosStranicaA = int(input("Duljina stranice a: "))
unosStranicaB = int(input("Duljina stranice b: "))
unosStranicaC = int(input("Duljina stranice c: "))

if(unosStranicaA + unosStranicaB > unosStranicaC and 
   unosStranicaA + unosStranicaC > unosStranicaB and 
   unosStranicaC + unosStranicaB > unosStranicaA):

    if(unosStranicaA == unosStranicaB == unosStranicaC):
        print("Jednakostranican trokut")

    elif(unosStranicaA == unosStranicaB or 
         unosStranicaA == unosStranicaC or 
         unosStranicaB == unosStranicaC):

        print("Jednakokračan trokut")
        
    else:
        print("Raznostraničan trokut")
else:
    print("Unesene duljine stranica ne čine trokut.")