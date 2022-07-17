k = 0
mch = 123123
for i in range(10001, 50001):
    kd = 2
    for d in range(2, i//2+1):
        if i % d == 0:
            kd += 1
    if kd > 17:
        k += 1
        mch = min(mch, i)
print(k, mch)

