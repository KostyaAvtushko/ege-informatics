f = open("24-2509.txt").readline()

s = []
for i in range(65, 91):
    s.append(f.count(chr(i)))
print(max(s) - min(s))





