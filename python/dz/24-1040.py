f = open("24-1040.txt").readline()

k = 0
rk = 0

for i in range(0, len(f)):
    if f[i] in "1234567890":
        k += 1
        rk = max(rk, k)
    else:
        k = 0
print(rk)




