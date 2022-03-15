for a in range(1, 100):
    ok = 1
    for x in range(0, 100):
        for y in range(0, 100):
            if not((2*x + 3*y < 30) or (x + y >= a)):
                ok = 0
    if ok == 1:
        print(a)