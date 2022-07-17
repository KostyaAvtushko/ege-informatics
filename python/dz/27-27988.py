f = open('27-27988.txt')
n = int(f.readline())
s = [int(i) for i in f]

mk2 = 0
mk13 = 0
mk26 = 0
m = 0

for i in range(n):
    if s[i] % 26 == 0:
        if mk26 < s[i]:
            mk26 = s[i]
    else:
        if s[i] % 13 == 0:
            mk13 = max(mk13, s[i])
        if s[i] % 2 == 0:
            mk2 = max(mk2, s[i])
        m = max(s[i], m)
print(max(mk26*m, mk13*mk2))
