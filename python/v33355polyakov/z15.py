for a in range(1, 100):
    ok = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not((y + 3 * x < a) or (x > 9) or (y > 20)):
                ok = False
    if ok:
        print(a)