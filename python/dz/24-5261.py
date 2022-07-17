f = open("24-5261.txt").readline()

k = 0
rk = 0

for i in range(0, len(f)-2):
    if (f[i] == "A" and f[i+1] == "B") or (f[i] == "B" and (f[i+1] == "A" or f[i+1] == "C")) or (f[i] == "C" and f[i+1] == "B"):
        k += 1
        rk = max(k, rk)
    else:
        k = 0
print(rk, len(f))



