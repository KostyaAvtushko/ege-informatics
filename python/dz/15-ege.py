for a in range(1, 1000):
    ok = 1
    for b in range(50, 61):
        for x in range(1, 1000):
            if not((x % a == 0) or ((x % b == 0) <= (x % 13 != 0))):
                ok = 0
    if ok:
        print(a)
