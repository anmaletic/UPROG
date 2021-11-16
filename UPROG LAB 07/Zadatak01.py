# Uđite u Python Shell. Uvezite modul math (import math) i zatražite help(math). Pregledajte koje
# sve funkcije možete pozvati iz tog modula i pregledajte malo kratku dokumentaciju, tj. docstring
# pojedinih funkcija. Zatražite opis (atribut) funkcije sa: print(math.sqrt.__doc__), a zatim sa
# help(math.sqrt). Da ne biste morali pisati ime modula, napišite naredbu from math import *. Sad
# su vam sve funkcije modula math dostupne direktno. Napišite print(sqrt.__doc__), help(sqrt).
# Zatražite isto za funkcije ceil i floor. Da li iz opisa, tj. iz dokumentacijskog stringa, možete
# razumjeti što te funkcije rade? Isprobajte ih na decimalnim brojevima.
# Primjetite da docstring počinje velikim slovom i završava točkom, pa i vi svoj pišite tako.
# Definirajte sada u Shell- u funkciju koja prima dva broja (ima dva parametra) i vraća njihov zbroj.
# Pozovite je te potom zatražite help za tu funkciju i atribut __doc__.

from math import *

print(sqrt.__doc__)
print(ceil.__doc__)
print(floor.__doc__)


def Zbroj(a, b):
    '''Vraca zbroj dva broja.'''    
    return a + b

help(Zbroj)
print(Zbroj.__doc__)
print()

unosA = int(input("Prvi broj: "))
unosB = int(input("Drugi broj: "))

z = Zbroj(unosA, unosB)

print(F"{unosA} + {unosB} = {z}")