f = open('24-kim11980.txt').readline()
f = f.replace('XXY', '*').replace('XZY', '*').replace('XYY', '*').replace('ZXY', '*').replace('ZYY', '*').replace('ZZY', '*')

k = 0
rk = 0

for i in range(0, len(f)):
    if f[i] == '*':
        k += 1
        rk = max(k, rk)
    else:
        k = 0

print(rk)


