f = open("26-kim11979.txt")
k, n = (map(int, f.readline().split()))
napr = []
for j in range(k):
    napr.append(int(f.readline()))
a = [0]*k
n15 = []
for i in range(n):
    y = f.readline().split()
    naprs = int(y[1])
    if naprs == 15:
       n15.append(int(y[0]))
    a[naprs] += 1
sumpost = 0

for g in range(len(napr)):
    if a[g] > napr[g]:
        sumpost += napr[g]
    else:
        sumpost += a[g]
maxotn = 0
mpnapr = 0
for h in range(len(napr)):
    if a[h] != 0:
        if a[h]/napr[h] > maxotn:
            maxotn = a[h]/napr[h]
            mpnapr = h
print(a)
print(napr)
print(sumpost)
print(mpnapr)
print(maxotn)
print(a[15], napr[15])

print(sorted(n15)[408:])
print(len(sorted(n15)[408:]))

