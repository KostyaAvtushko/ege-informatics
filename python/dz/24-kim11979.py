f = open('24-kim11979.txt').readline()

k = 0
rk = 0
ka = 0

for i in range(0, len(f)):
    if f[i] != ".":
        k += 1
        if f[i] == "A":
            ka += 1
        if ka >= 3:
            rk = max(k, rk)
    if f[i] == ".":
        k = 0
        ka = 0
    print(ka)
print(rk)


