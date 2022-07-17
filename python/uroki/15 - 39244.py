for a in range(0, 1000):
    ok = 1
    for x in range(0, 1000):
        if not((x & 105 == 0) <= ((x & 58 != 0) <= (x & a != 0))):
            ok = 0
    if ok == 1:
        print(a)