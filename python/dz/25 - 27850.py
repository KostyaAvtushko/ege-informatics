def isSimple(p):
    res = True
    d = 2
    if p % d == 0:
        return p == 2
    d = 3
    while d <= int(p**0.5):
        if p % d == 0:
            res = False
            break
        d += 2
    return res


simples = []
numbers = []
for i in range(245690, 245756):
    if isSimple(i):
        simples.append(i)
        numbers.append(i - 245689)
print(simples)
print(numbers)
