f = open("24-4042.txt")
s = []
for line in f:
    s.append(line)
mr = 0
y = []
for i in s:
    print(i)
    if i.count("E") < 20:
        y.append(i)
        for j in range(65, 92):
            mr = max(mr, i.rfind(chr(j)) - i.find(chr(j)))
            print(i, '\n', mr, '\n', j, i.rfind(chr(j)) - i.find(chr(j)))
print(mr)
