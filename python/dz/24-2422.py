f = open("24-2422.txt").readline()

k = 1
rk = 1

for i in range(1, len(f)):
    if ord(f[i]) - ord(f[i-1]) == 1 or ord(f[i]) - ord(f[i-1]) == 0:
        k += 1
        rk = max(k, rk)
    else:
        k = 1
print(rk)







