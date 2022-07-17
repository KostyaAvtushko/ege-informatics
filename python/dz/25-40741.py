for i in range(10000000, 10100000):
    dels = []
    for d in range(2, int(i**0.5)):
        if i % d == 0:
            dels.append(d)
            dels.append(i//d)
    if len(dels) >= 2:
        md = max(dels)
        dels.remove(md)
        md2 = max(dels)
        if (0 < (md + md2)) and ((md + md2) < 10000):
            print(md + md2, i)
