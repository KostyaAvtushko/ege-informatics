
for i in range(700000, 1000000):
    sd = 0
    for d in range(2, int(i**0.5)+1):
        if i % d == 0:
            d2 = i // d
            sd = d + d2
            break
    if str(sd)[len(str(sd))-1] == '8':
        print(i, sd)