
f = open("24-2499.txt").readline()

k = 0
for i in range(3, len(f)):
    if f[i-3] + f[i-2] + f[i-1] + f[i] == "XXXX":
        k += 1
print(k)



