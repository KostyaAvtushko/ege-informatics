f = open("24-2502.txt")
s = []
for line in f:
    s.append(line)

k = 0
for i in s:
    p = 0
    for j in range(3, len(i)):
        if i[j-3] + i[j-1] + i[j] == "KGE":
            p = 1
    if p == 1:
        k += 1
print(k)



