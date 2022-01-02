# Što će biti ispisano:

s = 'Kolokviji'
s1 = ''
for i in range (len(s)-1):
    s1 = s1 + s[i]
    if s[i] in 'aeiou':
        s1 = s1 + '-'
s1 += s[-1]
print(s1)

# Ko-lo-kvi-ji