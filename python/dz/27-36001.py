f = open("27-36001.txt")
n = int(f.readline())

sb = []
sm = []

min1 = 10**10
min2 = 10**10
min3 = 10**10

for i in range(n):
    a = list(map(int, f.readline().split()))
    if a[0] % 2 != 0:
        if a[0] % 2 != 0 and a[1] % 2 != 0:
            min1 = min(a[0] + a[1], min1)
        if min(a) % 2 != 0 and max(a) % 2 == 0:
            min2 = min(a[0] + a[1], min2)
        if min(a) % 2 == 0 and max(a) % 2 != 0:
            min3 = min(a[0] + a[1], min3)
        sb.append(max(a))
        sm.append(min(a))
if sum(sm) % 2 != 0 and sum(sb) % 2 == 0:
    print(sum(sm) + sum(sb) - min(min1, min2 + min3))
if sum(sm) % 2 != 0 and sum(sb) % 2 != 0:
    print(sum(sm) + sum(sb) - min(min2, min1 + min3))
if sum(sm) % 2 == 0 and sum(sb) % 2 == 0:
    print(sum(sm) + sum(sb) - min(min3, min1 + min2))
if sum(sm) % 2 == 0 and sum(sb) % 2 != 0:
    print(sum(sm) + sum(sb))


