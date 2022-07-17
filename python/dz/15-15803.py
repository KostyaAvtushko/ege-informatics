for a in range(1, 1000):
    ok = 1
    for x in range(0, 1000):
        if not((a <= (x**2 <= 100)) and ((x**2 <= 64) <= a)):
            ok = 0
    if ok == 1:
        print(a)