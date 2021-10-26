#   Napišite program za izračun i ispis trajanja filma u satima i minutama. Vrijeme početka i završetka
#   filma unosi se u satima i minutama (podrazumijeva se da je film započeo i završio u istom danu).


class FilmoviModel:
    def __init__(self, Sati, Minute):
        self.Sati = Sati
        self.Minute = Minute
    
    def GetTotalMinute(self):
        return self.Sati * 60 + self.Minute

    def GetTrajanje(self, Pocetak, Kraj):
        TotalMin = Kraj.GetTotalMinute() - Pocetak.GetTotalMinute()
        self.Sati = TotalMin // 60
        self.Minute = TotalMin % 60

PocetakFilma = FilmoviModel(0, 0)
KrajFilma = FilmoviModel(0, 0)
TrajanjeFilma = FilmoviModel(0, 0)

print("Unesite vrijeme pocetka filma: ")
PocetakFilma.Sati = int(input("Sat: "))
PocetakFilma.Minute = int(input("Minute: "))

print("")

print("Unesite vrijeme kraja filma: ")
KrajFilma.Sati = int(input("Sat: "))
KrajFilma.Minute = int(input("Minute: "))

print("")

TrajanjeFilma.GetTrajanje(PocetakFilma, KrajFilma)

print(F"Trajanje filma: {TrajanjeFilma.Sati}h {TrajanjeFilma.Minute}min")