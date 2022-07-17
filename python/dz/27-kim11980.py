import functools
import math
f = open('27-kim11980.txt')
n, k = map(int, f.readline().split())
s = [int(i) for i in f]

nod = 0

for i in range(n):
    for j in range(i+1, n):
        nod = max(functools.reduce(math.gcd, s[i:j]), nod)

print(nod)





