k = 0
mch = 12313123
for i in range(5913, 11754):
    if i % 5 == 0 and i % 11 == 0 and i % 7 != 0 and i % 10 != 0 and i % 13 != 0 and i % 22 != 0:
        k += 1
        mch = min(i, mch)
print(k, mch)