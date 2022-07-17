f = open("p-17v-24ch.txt").read()

mk = ""
k = ""

for i in range(0, len(f)):
    if ord(f[i]) - ord(f[i-1]) == 1:
        k += f[i] + f[i-1]
        if len(k) >= len(mk):
            mk = k
    else: k = ""
print(mk)
print(ord('O'))
print(ord('N'))
print(ord('M'))