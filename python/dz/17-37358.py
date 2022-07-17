f = open("uroki/17txt/17-37358.txt")
a = []
for line in f:
    a.append(int(line))
k = 0
ms = 0
n = len(a)
for i in range(0, n-1):
    for j in range(i+1, n):
        if (a[i]+a[j]) % 10 == 0:
            k += 1
            if a[i] + a[j] > ms:
                ms = a[i] + a[j]
print(k, ms)