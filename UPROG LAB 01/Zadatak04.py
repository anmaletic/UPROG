# Napišite program koji od korisnika traži unos radijusa kruga te potom izračunava i ispisuje 
# opseg i površina kruga.

import math

pi = math.pi

r_kruga = float(input("Unesite radijus kruga: "))

o_kruga = 2 * r_kruga *  pi
p_kruga = r_kruga ** 2 * pi

print("-" * 32)

print("Opseg kruga je: ", o_kruga)
print("Površina kruga je: ", p_kruga)