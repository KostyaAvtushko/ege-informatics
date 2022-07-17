f = open("C:/Users/avtus/Downloads/24 (26).txt")
s = []
for line in f:
    s.append(line)

k = 0
for i in s:
    if i.count("B")/i.count("A") >= 1.05:
        k += 1
print(k)



