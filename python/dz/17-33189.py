k = 0
mch = 123123
dels = [11, 13, 17, 19]
for i in range(11000, 22001):
    kd = 0
    for d in dels:
        if i % d == 0:
            kd += 1
    if kd == 2:
        k += 1
        mch = min(mch, i)
print(k, mch)