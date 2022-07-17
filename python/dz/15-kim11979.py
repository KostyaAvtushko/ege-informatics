for a in range(1, 100):
    ok = 1
    for x in range(0, 100):
        if not(((x % 2 == 0) <= (x % 5 != 0)) or (x + a >= 90)):
            ok = 0
    if ok:
        print(a)

