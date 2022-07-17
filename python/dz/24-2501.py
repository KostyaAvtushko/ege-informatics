f = open("24-2501.txt").readline()

k = 0
for i in range(4, len(f)):
    if f[i-4] + f[i-2] + f[i] == "AAA":
        k += 1
print(k)



