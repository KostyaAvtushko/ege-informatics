for a in range(1, 1000):
    ok = 1
    for x in range(1, 1000):
        if not((a % 40 == 0) and (780 % x == 0) <= ((a % x != 0) <= (180 % x != 0))):
            ok = 0
    if ok == 1:
        print(a)