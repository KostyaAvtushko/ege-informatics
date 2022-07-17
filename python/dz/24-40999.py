f = open("24-40999.txt")
s = f.read()
k = 0
ro = ""
o = ""
for i in range(0, len(s)):
    if s[i] != 'E':
        o = o + s[i]
    if s[i] == 'E':
        if len(o) > len(ro) and s.count('A') >= 3:
            ro = o
        o = ""
print(ro)
print(len(ro))