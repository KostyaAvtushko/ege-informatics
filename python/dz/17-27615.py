k = 0
mch = 123123
for i in range(3521, 13020):
    if i % 9 == 0 and i % 15 == 0 and i % 6 != 0 and i % 12 != 0 and i % 17 != 0 and i % 21 != 0:
        k += 1
        mch = min(mch, i)
print(k, mch)