res = 0
gkd = 0
for u in range(120115, 120200):
    kd = 1
    x = u
    for d in range(1, x):
        if x % d == 0:
            kd += 1
    if kd > gkd:
        gkd = kd
        res = x

print(gkd, res)
