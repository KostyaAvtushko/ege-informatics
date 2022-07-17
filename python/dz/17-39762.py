f = open('17-39762.txt')
s = []
for line in f:
    s.append(int(line))
ms = 0
k = 0
for i in range(1, len(s)):
    if (s[i]*s[i-1]) % 15 == 0 and (s[i] + s[i-1]) % 7 == 0:
        k += 1
        ms = max(ms, s[i] + s[i-1])
print(k, ms)