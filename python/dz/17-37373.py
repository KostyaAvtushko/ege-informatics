f = open('17-37373.txt')
s = []
for line in f:
    s.append(int(line))
k = 0
mr = 0
for i in range(0, len(s)-1):
    for j in range(i+1, len(s)):
        if (s[i] - s[j]) % 36 == 0 and (s[i] % 13 == 0 or s[j] % 13 == 0):
            k += 1
            mr = max(mr, s[i] - s[j])
print(k, mr)