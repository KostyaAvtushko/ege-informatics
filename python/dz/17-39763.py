f = open("uroki/17txt/17-39763.txt")
a = []
for line in f:
    a.append(int(line))
k = 0
ms = 0
n = len(a)
for i in range(0, n-2):
    b = [0, 0, 0]
    b[0] = a[i]
    b[1] = a[i+1]
    b[2] = a[i+2]
    b.sort()
    if b[2]**2 < b[1]**2 + b[0]**2:
        k += 1
        if sum(b) > ms:
            ms = sum(b)
print(k,ms)