f = open("17-kim4839.txt")
s = []
for line in f:
    s.append(int(line))
kp = 0
ms = 0
for i in range(1, len(s)):
    if (s[i] % 3 == 0) or (s[i-1] % 3 == 0):
        kp += 1
        ms = max(s[i] + s[i-1], ms)
print(kp, ms)