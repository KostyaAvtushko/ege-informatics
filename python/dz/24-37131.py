f = open("24-37131.txt").read()

k = 1
rk = 1
for i in range(1, len(f)):
    if (f[i] + f[i-1] != "KL") and (f[i] + f[i-1] != "LK"):
        k += 1
        rk = max(k, rk)
    else:
        k = 1
print(rk)