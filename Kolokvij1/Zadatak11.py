
def GetDjelitelj(x, y):

    dx = []
    dy = []
   
    _d = 2

    while True:
        if(x % _d == 0):
            dx.append(_d)
            x = x // _d
        else:
            _d += 1

            if(_d > x):
                break

    _d = 2

    while True:
        if(y % _d == 0):
            dy.append(_d)
            y = y // _d
        else:
            _d += 1

            if(_d > y):
                break

    dRange = len(dx)
    if(len(dy) < len(dx)):
        dRange = len(dy)

    D = 1
    for i in range(dRange):
        if(dx[i] == dy[i]):
            D = D * dx[i]

    print(*dx)
    print(*dy)
    print(F"{dRange}")
    print(D)

    
unosBrojX = int(input("Upisite prvi broj: "))
unosBroyY = int(input("Upisite drugi broj: "))

GetDjelitelj(unosBrojX, unosBroyY)

# 456 96