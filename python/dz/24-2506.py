f = open("24-2506.txt").readline()

s = []
for i in range(65, 91):
    s.append(f.count(chr(i)))
print(max(s), s.index(max(s)))
print(chr(65+22))