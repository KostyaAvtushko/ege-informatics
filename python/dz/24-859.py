f = open("24-859.txt")
s = []
for line in f:
    s.append(line)

k = 0
for i in s:
    if i.count("S") == i.count("X"):
        k += 1
print(k)



