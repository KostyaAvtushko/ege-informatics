from statistics import mode
f = open("24-33196.txt").read()

s = []
for i in range(0, len(f)):
    if f[i] == "A":
        s.append(f[i + 1])
print(mode(s))