for a in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        if not((x & 49 != 0) <= ((x & 41 == 0) <= (x & a != 0))):
            ok = False
    if ok == True:
        print(a)