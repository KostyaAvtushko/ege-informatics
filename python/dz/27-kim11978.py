
f = open('27-kim11978.txt')
n, k = map(int, f.readline().split())
print(n, k)
s = [int(i) for i in f]

g = []
r = 0
for i in range(n-k):
    g = []
    for j in range(i, i + k):
        g.append(s[j])
    if sum(g[:5]) == sum(g[6:]):
        print(g)
        print(g[:5], g[6:])

        r += 1
print(r)