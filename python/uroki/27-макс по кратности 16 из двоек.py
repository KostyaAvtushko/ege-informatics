f = open('27-p2687.txt')
n = int(f.readline())

x = [0]*16 # предыдущие суммы
y = [0]*16 # текущие суммы

a = list(map(int, f.readline().split()))
for j in range(2):
    if y[a[j] % 16] < a[j]:
        y[a[j] % 16] = a[j]
print(a, y)
for i in range(1, n):
    a = list(map(int, f.readline().split()))
    for j in range(16):
        x[j] = y[j]
        y[j] = 0
    for k in range(16):
        if x[k] > 0:
            for p in range(2):
                z = x[k] + a[p]
                if y[z % 16] < z:
                    y[z % 16] = z
print(a, y)
y[10] = 0
print(y)
print(max(y))


