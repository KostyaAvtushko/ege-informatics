for i in range(101_000_000, 102_000_000):
    chdels = 0
    for d1 in range(1, int(i**0.5)+1):
        if i % d1 == 0:
            d2 = i // d1
            if d2 % 2 == 0:
                chdels += 1
            if d1 % 2 == 0:
                chdels += 1
            if d1 % 2 == 0 and d1 == d2:
                chdels -= 1
        if chdels > 3:
            break
    if chdels == 3:
        print(i, chdels)
