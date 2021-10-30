n = int(input('Unesite cijeli broj: '))
b = 1
while b < n:
    if b == int(n / 2):
        print('sada sam na sredini')
        continue

    print(b)
    b += 1
print('Izasao sam iz petlje')