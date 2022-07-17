f = open("27-29675.txt")
n = int(f.readline())


x = [0]*3
y = [0]*3
a = list(map(int, f.readline().split()))
for t in range(2):
    if y[a[t] % 3] < a[t]:
        y[a[t] % 3] = a[t]
print(a, y)
for i in range(1, n):
    a = list(map(int, f.readline().split()))
    for j in range(3):
        x[j] = y[j]
        y[j] = 0
    for g in range(3):
        if x[g] > 0:
            for p in range(2):
                z = a[p] + x[g]
                if y[z % 3] < z:
                    y[z % 3] = z

print(y)
print(y[0])