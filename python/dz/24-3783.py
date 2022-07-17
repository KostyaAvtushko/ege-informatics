import statistics

f = open("24-3783.txt")
s = []
for line in f:
    s.append(line)
mr = 10**10

for i in s:
    k = 0
    for j in range(1, len(i)):
       if ord(i[j]) - ord(i[j-1]) == 1:
            k += 1
    if 1 < k < mr:
        mr = k
y = []
for i in s:
    k = 0
    for j in range(1, len(i)):
       if ord(i[j]) - ord(i[j-1]) == 1:
            k += 1
    if k == mr:
        y.append(i)
h = 0
for i in s:
    h += i.count(statistics.mode(y[0]))
print(y[0])
print(statistics.mode(y[0]), h)
