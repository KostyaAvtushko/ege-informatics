f = open("24-kim11978.txt").readline()
print(len(f), f[:100])
f = f.replace('ZXY', '*').replace('ZYX', '*')

k = 0
rk = 0

for i in range(1, len(f)):
    if f[i] == "*":
        k += 1
        rk = max(k, rk)
    else:
        k = 0
print(rk)