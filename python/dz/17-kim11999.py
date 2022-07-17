f = open('17-kim11999.txt')
s = [int(i) for i in f]
m11 = 0
for j in s:
    if j % 11 == 0:
        m11 = max(j, m11)
print(m11)
k = 0
ms = 10**10
for i in range(1, len(s)):
    if (s[i] > m11) or (s[i-1] > m11):
        k += 1
        ms = min(ms, s[i] + s[i-1])
print(k, ms)