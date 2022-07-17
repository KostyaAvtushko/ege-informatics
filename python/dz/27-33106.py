f = open("27-33106.txt")
n = int(f.readline())

dmin = 10**9
s = 0

for i in range(n):
    a = list(map(int, f.readline().split()))
    s += min(a)
    if dmin > (max(a) - min(a)) and (max(a) - min(a)) % 3 == 1:
        dmin = max(a) - min(a)
print(dmin)
if s % 3 == 0:
    print(s)
else:
    print(s + dmin)