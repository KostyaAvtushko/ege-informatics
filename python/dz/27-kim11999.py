f = open("27-kim11999.txt")
n, k = map(int, f.readline().split())
s = [int(i) for i in f]
# ms = 0
# spp = s[0]
# t = 0
# y = 0
# my = 0
#
# fch = s[t]
# for i in range(n):
#     if spp + s[i] <= k:
#         spp += s[i]
#         ms = max(spp, ms)
#         y += 1
#         my = max(my, y)
#     if (spp + s[i] > k) and (spp - fch + s[i] <= k):
#         spp = spp - fch + s[i]
#         ms = max(spp, ms)
#         t += 1
# print(my, sum(s[:50]))
y = 0
ms = 0
for i in range(n):
    for j in range(i+1, n):
        if sum(s[i:j]) <= k:
            y += 1
            ms = max(ms, len(s[i:j]))
print(ms, y)