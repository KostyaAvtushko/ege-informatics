f = open("24-27694.txt").readline()

k = 0
mp = 0

for i in range(0, len(f)):
    if f[i] == 'A' and f[i+1] == 'B':
        k += 1
        mp = max(mp, k)
    if f[i] == 'B':
        continue
    if f[i] == 'C':
        continue
    if f[i] == 'A' and f[i+1] != 'B':
        k += 1
        mp = max(mp, k)
        k = 1

print(mp)