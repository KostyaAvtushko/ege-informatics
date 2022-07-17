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

kk = 0

for i in range(1060, 188138):
    if isSimple(i):
      kk += i
print(kk)