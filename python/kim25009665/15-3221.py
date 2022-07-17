for a in range(1, 100):
    ok = True
    for x in range(1, 100):
        if not(((x % 3 == 0) <= (x % 5 != 0)) or (x + a >= 70)):
            ok = False
    if ok:
        print(a)