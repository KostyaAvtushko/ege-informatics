f = open("p-17v-17ch.txt")
s = []
for line in f:
    s.append(int(line))
k = 0

sm = 0
for i in range(2, len(s)):
    if ((s[i] % 16 == 0) and (s[i-1] % 16 == 0)) or ((s[i-2] % 16 == 0) and (s[i-1] % 16 == 0)) or ((s[i] % 16 == 0) and (s[i-2] % 16 == 0)):
        k += 1
        sm += max(s[i], s[i-1], s[i-2])

print(k, sm)