#   U semestru imate pet predmeta označenih brojevima od 1 do 5. Iz jednog predmeta ocjena nije 
#   zaključena i redni broj tog predmeta se ne unosi. Program na kraju ispisuje redni broj predmeta za 
#   koji nije zaključena ocjena. Podrazumijeva se da su brojevi ispravno uneseni.

class PredmetiModel:
    def __init__(self, Naziv, Status):
        self.Naziv = Naziv
        self.Status = Status
        
    def SetZakljuceno(self):
        self.Status = True    

#   predmeti = [ PredmetiModel(1, False), PredmetiModel(2, False),  PredmetiModel(3, False), PredmetiModel(4, False), PredmetiModel(5, False) ]

predmeti = []

for i in range(5):
    predmeti.append(PredmetiModel(i+1, False))

def GetZakljuceno(list):
    for PredmetiModel in list:
        if(PredmetiModel.Status == False):
            return PredmetiModel.Naziv        

for i in range(4):
    
    unos = int(input("Unesite redni broj predmeta: "))
    predmeti[unos-1].SetZakljuceno()

print("Preostali predmet je: ", GetZakljuceno(predmeti)) 