f = open("uroki/17txt/17-40992.txt")
a = []
for line in f:
    a.append(int(line))
k = 0
ms = 0
countNech = 0
n = len(a)
sumA = 0
for x in a:
    if x % 2 != 0:
        sumA += x
        countNech += 1
arifA = sumA / countNech
for i in range(0, n-1):
    if (a[i] < arifA or a[i+1] < arifA) and (a[i] % 5 == 0 or a[i+1] % 5 == 0):
        k += 1
        if a[i] + a[i+1] > ms:
            ms = a[i] + a[i+1]
print(k, ms)