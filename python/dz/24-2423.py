f = open("24-2423.txt").readline()

k = 1
rk = 1

for i in range(1, len(f)):
    if f[i] == "\n":
        continue
    if int(f[i]) - int(f[i-1]) == 1:
        k += 1
        rk = max(k, rk)
    else:
        k = 1
print(rk)







