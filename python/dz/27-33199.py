f = open("27-33199.txt")
n = int(f.readline())

s1 = 0
s2 = 0
s3 = 0

for i in range(n):
    a = list(map(int, f.readline().split(" ")))
    s1 += max(a)
    s2 += min(a)
    s3 += sum(a) - max(a) - min(a)

print(s1, s2, s3)