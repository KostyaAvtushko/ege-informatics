f = open("24-2503.txt")
s = []
for line in f:
    s.append(line)

k = 0
for i in s:
    if i.count("AOA") > i.count("OAO"):
        k += 1
print(k)



