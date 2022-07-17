for i in range(500000, 1000000):
    for d in range(9, i//2):
        if i % d == 0 and str(d)[len(str(d))-1] == "8":
            print(d, i)
