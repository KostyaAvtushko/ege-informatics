f = open("24-33103.txt").read()

s = f.split("\n")

kk = 0

for i in s:
    a = i.count('A')
    e = i.count('E')
    if a > e:
        kk += 1

print(kk)