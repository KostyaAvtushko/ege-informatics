k = 0
mch = 0
for i in range(8812, 12286):
    if (i % 8 == 0 or i % 19 == 0)  and (i % 4 != 0 and i % 9 != 0 and i % 14 != 0 and i % 16 != 0):
        k += 1
        mch = max(mch, i)
print(k, mch)