k = 0
for i in range(1, 10000):
    s = i
    s = s // 11
    n = 9
    while s < 203:
        if (s + n) % 5 == 0:
            s = s + 6
        n = n + 13
    if n == 126:
        k += 1
print(k)



