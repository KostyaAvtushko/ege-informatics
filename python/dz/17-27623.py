k = 0
mch = 123123
for i in range(4855, 7856):
    if i % 8 == 0 and i % 19 == 0 and i % 7 != 0 and i % 16 != 0 and i % 24 != 0 and i % 26 != 0:
        k += 1
        mch = min(mch, i)
print(k, mch)