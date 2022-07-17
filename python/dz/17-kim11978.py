f = open("17-11978.txt")
s = [int(i) for i in f]
m111 = 0
for j in s:
    if j % 111 == 0:
        m111 = max(j, m111)

kp = 0
ms = 10**10
for i in range(1, len(s)):
    if ((s[i] > m111) or (s[i-1] > m111)) and ((s[i] % 10 == 7) or (s[i-1] % 10 == 7)):
        kp += 1
        ms = min(ms, s[i] + s[i-1])
print(kp, ms)