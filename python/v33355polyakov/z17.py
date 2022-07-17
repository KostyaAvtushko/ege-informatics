f = open('17-5.txt')
s = []
for line in f:
    s.append(int(line))

ms = 0
k = 0

for i in range(1, len(s)):
    if s[i] % 2 == 0 or s[i-1] % 2 == 0:
        k += 1
    if s[i] + s[i-1] > ms:
        ms = s[i] + s[i-1]
print(k, ms)