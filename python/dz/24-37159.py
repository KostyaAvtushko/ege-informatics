f = open('24-37159.txt').read()
k = 1
mk = 0
for i in range(1, len(f)):
    if f[i] + f[i-1] != "ad" and f[i] + f[i-1] != "da":
        k += 1
        mk = max(k, mk)
    else:
        k = 1
print(mk)