f = open("24-38958.txt").readline()
f = f.split("A")
print(f[:20])
ms = 0
for i in range(1, len(f)):
    ms = max(ms, len(f[i]) + len(f[i-1]))
print(ms + 1)#прибавляем А
