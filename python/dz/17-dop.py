f = open("taskvar123.txt")
s = []
for line in f:
    s.append(int(line))
u = []
for j in s:
    if j % 10 == 0:
        u.append(j)
mch = min(u)
k = 0
ms = -123123123
for i in range(1, len(s)):
    if ((str(s[i])[len(str(s[i]))-1] == "7") or (str(s[i-1])[len(str(s[i-1]))-1] == "7")) and ((s[i] + s[i-1]) < mch):
        k += 1
        ms = max(ms, s[i] + s[i-1])
print(k, abs(ms))
