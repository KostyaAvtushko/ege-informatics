for u in range(45000000, 50000000):
    kd = 0
    x = u
    if x % 100000 == 0:
        print('===', x)
    for d1 in range(1, int(x**0.5)+1):
        if x % d1 == 0:
            d2 = x // d1
            if d1 % 2 != 0:
                kd += 1
            if d2 % 2 != 0:
                kd += 1
            if d1 == d2 and d1 % 2 != 0:
                kd -= 1
        if kd > 5:
            break
    if kd == 5:
        print(u)



