f = open("24-11999.txt").readline()
f = f.replace("BB", "*").replace("DD", "1").replace("A", " ")
print(f)
kb = 0
rkb = 0
kd = 0
rkd = 0
for i in range(0, len(f)):
    if f[i] == "*":
        kb += 1
        rkb = max(rkb, kb)
    else:
        kb = 0
    if f[i] == "1":
        kd += 1
        rkd = max(rkd, kd)
    else:
        kd = 0
print(rkd + rkb)
