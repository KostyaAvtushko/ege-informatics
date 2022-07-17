f = open("24-2498.txt").readline()

k = 0
for i in range(2, len(f)):
    if f[i-2] + f[i-1] + f[i] == "XIX":
        k += 1
print(k)



