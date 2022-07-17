f = open("24-2427.txt").readline()

k = f[0]
rk = f[0]

for i in range(1, len(f)):
    if ord(f[i-1]) - ord(f[i]) > 0:
        k += f[i]
        rk = max(k, rk, key=len)
    else:
        k = f[i]
print(rk)








