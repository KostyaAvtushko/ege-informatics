f = open("24-5155.txt").readline()
f = f.replace("B", " ")

kc = 0
ka = 0
rkc = 0
rka = 0
kac = 0
rkac = 0

for i in range(0,len(f) - 1, 2):
    if f[i] == "C" and f[i + 1] == "C":
        kc += 1
        rkc = max(rkc, kc)
    else:
        kc = 0
print(rkc, len(f))
for i in range(0,len(f) - 1, 2):
    if f[i] == "A" and f[i + 1] == "A":
        ka += 1
        rka = max(rka, ka)
    else:
        ka = 0
print(rkc, rka)

for i in range(0,len(f) - 1, 2):
    if (f[i] == "A" and f[i + 1] == "A") or  (f[i] == "C" and f[i + 1] == "C"):
        kac += 1
        rkac = max(rkac, kac)
    else:
        kac = 0
print(rkc, rka, rkac)



