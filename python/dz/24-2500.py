f = open("24-2500.txt").readline()

k = 0
for i in range(3, len(f)):
    if f[i-3] + f[i-1] + f[i] == "GME":
        k += 1
print(k)



