f = open("24-2251.txt").readline()
f = f.split("D")
m = 0
for i in range(len(f)-3):
    sub = f[i] + "D" + f[i+1] + "D" + f[i+2]
    m = max(m, len(sub))
print(m)