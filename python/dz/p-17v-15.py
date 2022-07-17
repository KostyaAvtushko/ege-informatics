for a in range(1, 100000):
    ok = True
    for x in range(0, 100):
        if not(((x % 16 != 0) == (x % 24 == 0)) <= (x % a == 0)):
            ok = False
    if ok:
        print(a)