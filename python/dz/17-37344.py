f = open('17-37344.txt')
s = []
for line in f:
    s.append(int(line))
k = 0
ms = 0
for i in range(0, len(s)-1):
    for j in range(i+1, len(s)):
        if (s[i] * s[j]) % 10 == 0:
            k += 1
            ms = max(ms, s[i] + s[j])
print(k, ms)