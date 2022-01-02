# Što će biti ispisano:

s1 = '2 + 3 = 4 + 1'
print(s1[:5])                       #   2 + 3
print(s1[8:])                       #   4 + 1
print(s1[4:5])                      #   3
print(s1[4:9])                      #   3 = 4
print(s1[-1])                       #   1
print(s1[-5:])                      #   4 + 1
print(s1.find('5'))                 #   -1
print(s1.find('+'))                 #   2
print(s1.replace('+', '*'))         #   2 * 3 = 4 * 1