f = open('17-kim11980.txt')
s = [int(i) for i in f]

srf = sum(s)/len(s)
k = 0
ms = 0
for i in range(1, len(s)):
    if (s[i] < srf) and (s[i-1] < srf) and ((s[i] % 10 == 9) or (s[i-1] % 10 == 9)):
        k += 1
        ms = max(ms, s[i] + s[i-1])
print(k, ms)