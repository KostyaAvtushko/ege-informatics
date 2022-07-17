f = open('17-dosrok-polyakov.txt')
s = []
for line in f:
    s.append(int(line))
ms = 0
kp = 0
min17 = 123123123
for c in s:
    if c % 17 == 0 and c < min17:
        min17 = c
for i in range(1, len(s)):
    if (s[i] % min17 == 0) or (s[i-1] % min17 == 0):
        kp += 1
        ms = max(ms, s[i]+s[i-1])
print(kp, ms)
