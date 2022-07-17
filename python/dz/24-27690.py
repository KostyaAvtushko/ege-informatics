f = open('24-27690.txt').read()

k = 1
rk = 0

for i in range(1, len(f)):
    if f[i-1] != f[i]:
        k += 1
        rk = max(rk, k)
    else:
        k = 1
print(rk)