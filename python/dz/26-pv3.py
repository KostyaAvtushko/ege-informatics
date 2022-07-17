f = open("26-pv3.txt")
v, k, n = map(int, f.readline().split(" "))
print(v, k, n)
a = [0]*k

files = sorted([int(i) for i in f], reverse=1)

j = 0
lp = []
for i in range(n):
    p = 0
    if files[i] <= (v - a[j]):
        a[j] += files[i]
        j += 1
        p = 1
    else:
        for u in range(k):
            if files[i] <= (v - a[u]):
                a[u] += files[i]
                j += 1
                p = 1
                break
    if p == 0:
        lp.append(files[i])
    if j == k:
        j = 0
print(a)
print(lp)
print(len(lp), sum(lp))