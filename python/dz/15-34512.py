for a in range(1, 100):
    ok = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not((x & 77 != 0) <= ((x & 12 == 0) <= (x & a != 0))):
                ok = False
    if ok:
        print(a)
