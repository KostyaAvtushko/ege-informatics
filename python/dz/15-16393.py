for a in range(1, 100):
    ok = True
    for x in range(0, 100):
        for y in range(0, 100):
            if not((2*x + 3*y > 30) or (x + y <= a)):
                ok = False
    if ok:
        print(a)