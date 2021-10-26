# Program učitava iznos dohotka za 50 zaposlenika. Nakon obrade ispisuje prosječnu vrijednost 
# dohotka, najveći i najmanji dohodak. Koristite for petlju.

dohodakSum = 0

for i in range(50):
    unosDohodak = float(input("Unesite dohodak za {}. zaposlenika: ".format(i+1)))

    if(i == 0):
        dohodakMax = unosDohodak
        dohodakMin = unosDohodak

    if(dohodakMin > unosDohodak):
        dohodakMin = unosDohodak
    elif(dohodakMax < unosDohodak):
        dohodakMax = unosDohodak

    dohodakSum += unosDohodak

print(F"Najveci dohodak: {dohodakMax} \nNajmanji dohodak: {dohodakMin} \nProsjecan dohodak: {round(dohodakSum / 50, 2)}")