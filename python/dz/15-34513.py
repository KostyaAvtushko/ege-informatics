for a in range(64):
    ok = 1
    for x in range(64):
        if not((x & 33 == 0) <= ((x & 45 != 0) <= (x & a != 0))):
            ok = 0
    if ok == 1:
        print(a)
        break
