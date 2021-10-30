# Program učitava osvojene bodove iz ispita za n studenata. Ispisuju se najveći i najmanji bodovi, te 
# prosijek bodova. Koristite for petlju . Podrazumijeva se da je korisnik unosio bodove iz raspona 0 –
# 100.

class StudentData():
    def GetMinBod(_student):
        _minBod = _student[0]
        for bod in _student:
            if(_minBod > bod):
                _minBod = bod
        return _minBod

    def GetMaxBod(_student):
        _maxBod = _student[0]
        for bod in _student:
            if(_maxBod < bod):
                _maxBod = bod
        return _maxBod 

    def GetProsjek(_student):
        _prosjek = 0
        for bod in _student:
            _prosjek += bod
        return _prosjek / len(_student)


unosBrojStudenata = int(input("Unesite broj studenata: "))

student = []

for i in range(unosBrojStudenata):
    unos = float(input(F"Unesite bodove {i+1}. studenta: "))
    student.append(unos)

print(F"Najmanji bodovi: {StudentData.GetMinBod(student)}")
print(F"Najveci bodovi: {StudentData.GetMaxBod(student)}")
print(F"Prosjek bodova: {StudentData.GetProsjek(student)}")
