f = open("24-5253.txt").readline()

k = ""
rk = 0
mk = 0
for i in range(0, len(f)):
    if k.count("2022") <= 4:
        k += f[i]
        if len(k) > rk:
            rk = len(k)
            mk = k
    else:
        k = ""
print(rk, len(f), mk.count("2022"))



