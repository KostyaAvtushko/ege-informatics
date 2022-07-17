#p = 2**x * a**4
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

a = 3
while a**4 <= 50000000:
    x = 0
    if isSimple(a):
        while 2**x * a**4 <= 50000000:
            if 2**x * a**4 >= 45000000:
                print(2**x*a**4, x, a)
            x += 1
    a += 2