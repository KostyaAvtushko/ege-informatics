f = open("uroki/17txt/17-37336.txt")
a = []
for line in f:
    a.append(int(line))
n = len(a)
print(a[:15], len(a))
k = 0
ms = 0
for i in range(0, n-1):
    if a[i] % 3 == 0 or a[i+1] % 3 == 0:
        k += 1
        if a[i] + a[i+1] > ms:
            ms = a[i] + a[i+1]
print(k, ms)