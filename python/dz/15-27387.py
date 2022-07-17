for a in range(1, 1000):
    ok = 1
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not((x * y < 120) or (y > a) or (x > a)):
                ok = 0
    if ok == 1:
        print(a)

