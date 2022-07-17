f = open("24-21.txt").readline()
k = 1
rk = 1
for i in range(1, len(f)):
    if f[i-1] != f[i]:
        k += 1
        rk = max(k, rk)
    else:
        k = 1
print(rk)







