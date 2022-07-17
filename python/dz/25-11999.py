for i in range(0, 1000000):
    a = "12"+str(i)+"6789"
    if int(a) % 39 == 0 and int(a) <= 10**8:
        print(a, int(a) / 39)