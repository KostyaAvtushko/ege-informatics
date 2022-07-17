import statistics

f = open("24-2505.txt").readline()
s = []
for i in range(2, len(f)):
    if f[i-2] == f[i]:
        s.append(f[i-1])
print(statistics.mode(s), s.count("W"))





