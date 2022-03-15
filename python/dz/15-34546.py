for a in range(1, 10000):
    ok = 1
    for p in range(23, 59):
        for q in range(1, 40):
            if not((p + a) <= (q + a)):
                ok = 0
    if ok == 1:
        print(a)
