f = open('17-kim11979.txt')
s = [int(i) for i in f]
m11 = 0
for j in s:
    if j % 11 == 0:
        m11 = max(j, m11)
k = 0
ms = 0

for i in range(1, len(s)):
    if (s[i] % 11 == 0 or s[i-1] % 11 == 0) and ((s[i] + s[i-1]) <= m11):
        k += 1
        ms = max(s[i] + s[i-1], ms)
print(k, ms)

