f = open("24-5230.txt").readline()
u = 0
k = ""
rk = 0
for i in range(0, len(f)):
    if f[i] == "A" or f[i] == "E" or f[i] == "I" or f[i] == "O" or f[i] == "U" or f[i] == "Y":
        u += 1
    if u <= 5:
        k += f[i]
        rk = max(len(k), rk)
    else:
        u = 0
        k = ""
print(rk, len(f))



