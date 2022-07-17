a = 6**203 + 5*6**405 - 3*6**144 + 76
s = []
while a > 0:
    s.append(a % 6)
    a //= 6
k = 0
for j in s:
    k += j
print(k)