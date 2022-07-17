f = open('24-36037.txt').readline()
mk = 0
k = 0
for i in range(2, len(f)):
    if f[i] == "X" and f[i - 1] == "Z" and f[i - 2] == "Z" and f[i - 3] == "Y":
        k = 0
    else:
        k += 1
        if k > mk:
            mk = k
print(mk)