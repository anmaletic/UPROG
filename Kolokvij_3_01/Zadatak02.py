# 2. 
# Desno od znaka komentara napišite što će biti ispisano:

gl = 'zvati'
L = list(gl)
print(L)                                        #   [z, v, a, t, i]
L1 = [znak for znak in L if znak in 'aeiou']
print(L1)                                       #   [a, i]
L2 = [znak * 2 for znak in L]
print(L2)                                       #   zz, vv, aa, tt, ii
L3 = [i for i in range(6) if i**2 == 2**i]
print(L3)                                       #   [2, 4]
L4 = [i-1 for i in range(5)]
print(L4)                                       #   [-1, 0, 1, 2, 3]