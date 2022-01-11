# Zadatak 4 
# Kreirajte klasu Krug koja ima atribut radijus. Koristite predefiniranu metodu __init__ (konstruktor). 
# Definirajte metode Opseg (2rPi) i Povrsina (r2Pi) koje vraćaju opseg i površinu kruga Stvorite dva objekta nad 
# tom klasom, prvom objektu neka radijus ima vrijednost predefiniranog parametra, a za drugi objektu 
# zatražite od korisnika unos vrijednosti radijusa. Ispišite opseg i površinu za oba kruga.

import math

class Krug():
    def __init__(self, radijus):
        self.r = radijus

    def Opseg(self):
        return round(2 * self.r * math.pi, 2)

    def Povrsina(self):
        return round(self.r ** 2 * math.pi, 2)

def main():
    krugConst = Krug(5)
    
    krugUser = Krug(float(input("Unesite radijus: ")))

    print(F"Opseg = {krugConst.Opseg()}")
    print(F"Povrsina = {krugConst.Povrsina()}")

    print(F"Opseg = {krugUser.Opseg()}")
    print(F"Povrsina = {krugUser.Povrsina()}")

main()