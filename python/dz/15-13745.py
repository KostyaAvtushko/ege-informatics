for a in range(1, 1000):
    ok = 1
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y <= 9))):
                ok = 0
    if ok == 1:
        print(a)