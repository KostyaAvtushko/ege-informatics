from statistics import mode
f = open("24-33526.txt").read()

s = []
for i in range(2, len(f)):
    if f[i] == f[i - 2]:
        s.append(f[i - 1])

print(mode(s))