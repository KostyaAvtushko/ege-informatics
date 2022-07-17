k = 0
for i in range(1, 10000):
    s = i
    s = s // 15
    n = 14
    while s < 285:
        if (s + n) % 9 == 0:
            s = s + 11
        n = n + 13
    if n == 118:
        k += 1
print(k)



