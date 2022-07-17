f = open('27-kim4839A.txt')
s = []
for line in f:
    s.append(int(line))
ms = 0
for i in range(1, len(s)):
    for j in range(1, len(s)):
        if sum(s[i:j]) % 43 == 0:
           ms = max(sum(s[i:j]), ms)
print(ms)