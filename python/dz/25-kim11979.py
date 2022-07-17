for i in range(220001, 1000000):
    sd = []
    for d in range(2, int(i**0.5)+1):
        if i % d == 0:
            sd.append(d)
            sd.append(i // d)
            break
    if sum(sd) % 10 == 4:
        print(i, sum(sd), sd)

