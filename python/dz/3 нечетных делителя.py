for i in range(101000000, 102000000):
    kd = 1
    for d in range(2, int(i**0.5)):
        if i % d == 0:
            d2 = i // d
            if d % 2 == 0 and d2 % 2 == 0:
                kd += 2
            elif d % 2 == 0 and d2 % 2 != 0:
                kd += 1
            elif d % 2 != 0 and d2 % 2 == 0:
                kd += 1
        if kd > 3:
            break
    if kd == 3:
        print(i)