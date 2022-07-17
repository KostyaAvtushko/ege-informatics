f = open("24-836.txt").readline()


k = 0
for i in range(4, len(f)):
    if f[i-4] + f[i-3] == f[i] + f[i-1]:
        k += 1
print(k)



