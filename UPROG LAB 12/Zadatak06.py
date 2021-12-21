# Zadatak 6
# Kreirajte klasu imena Student koja ima atribute: ime i prezime studenta, naziv predmeta te bodove 
# iz ispita. Koristite metodu __init__ za inicijalizaciju atributa.
# Klasa ima i metodu polozeno koji vraća tekst 'položeno' ako su bodovi veći ili jednaka 50, 'usmeni' 
# ako su bodovi veći ili jednaki 40 a manji od 50 te 'nepoloženo' za bodove manje od 40. Stvorite 
# objekt student1, unesite vrijednosti atributa i ispišite je li određeni student položio taj predmet. 
# Npr. za unos Ana Lovrić, UPROG, 40 ispis treba biti:
# student: Ana Lovrić
# predmet: UPROG
# stanje: usmeni

class Student():
    def __init__(self, ip, p, b):
        self.imePrezime = ip
        self.predmet = p
        self.bodovi = b

    def polozeno(self):
        if self.bodovi >= 50:
            return "položeno"
        elif self.bodovi >= 40:
            return "usmeni"
        else:
            return "nepoloženo"
    
student1 = Student("Ana Lovrić", "UPROG", 35)
print(F"Student: {student1.imePrezime}")
print(F"Predmet: {student1.predmet}")
print(F"Stanje: {student1.polozeno()}")
print()

studenti = []
studenti.append(Student("Ana Lovrić", "UPROG", 35))
studenti.append(Student("Ana Lovrić", "UPROG", 40))
studenti.append(Student("Ana Lovrić", "UPROG", 45))
studenti.append(Student("Ana Lovrić", "UPROG", 50))
studenti.append(Student("Ana Lovrić", "UPROG", 55))

for stud in studenti:
    print(F"Student: {stud.imePrezime}")
    print(F"Predmet: {stud.predmet}")
    print(F"Stanje: {stud.polozeno()}")
    print()