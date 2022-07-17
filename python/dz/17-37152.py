k = 0
mch = 0
for i in range(12972, 89323):
    if i % 13 == 7 and i % 7 != 0 and i % 11 != 0:
        k += 1
        mch = max(mch, i)
print(k, mch)