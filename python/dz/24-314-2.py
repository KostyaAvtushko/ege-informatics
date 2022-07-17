f = open("24-314.txt").readline()

k = 0

for i in range(4, len(f)):
    if f[i-2] + f[i-1] + f[i] == "OCK" and f[i-4] + f[i-3] + f[i-2] + f[i-1] + f[i] != "STOCK":
        k += 1
print(k)

