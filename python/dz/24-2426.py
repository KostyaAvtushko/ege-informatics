f = open("24-2426.txt").readline()

k = 0
rk = 0

for i in range(0, len(f)):
    if f[i] in "123":
        k += 1
        rk = max(rk, k)
    else:
        k = 0
print(rk)



