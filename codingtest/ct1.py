def isPalin(number):
    convert = str(number)
    return convert == convert[::-1]

print(isPalin(999999))

def largestPalin():
    arPalin = []
    arX = []
    arY = []

    for x in range(999,99,-1):
        for y in range(999,99,-1):
            if(isPalin(x * y)):
                arPalin.append(x * y)
                arX.append(x)
                arY.append(y)

    num = max(arPalin)
    x = arX[arPalin.index(max(arPalin))]
    y = arY[arPalin.index(max(arPalin))]
    return num, x, y

print(largestPalin())
