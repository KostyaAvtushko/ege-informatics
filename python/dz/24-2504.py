import statistics

f = open("24-2504.txt").readline()

s = []

for i in range(4, len(f)):
    if f[i-4] + f[i-3] + f[i-1] + f[i] == "CBBC":
        s.append(f[i-2])
print(statistics.mode(s), s.count(statistics.mode(s)))





