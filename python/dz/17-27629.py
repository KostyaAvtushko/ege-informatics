k = 0
mch = 123123
for i in range(1740, 14454):
    if i % 4 == 0 and i % 5 == 0 and i % 8 != 0 and i % 12 != 0 and i % 16 != 0 and i % 30 != 0:
        k += 1
        mch = min(mch, i)
print(k, mch)