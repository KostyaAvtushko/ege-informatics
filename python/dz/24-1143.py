f = open("24-1143.txt").readline()


k = 0
for i in range(0, len(f)):
    for j in range(i+7, i + 11):
        s = f[i:j]
        if s[0] == "A" and s[-1] == "F":
            k += 1
print(k)



