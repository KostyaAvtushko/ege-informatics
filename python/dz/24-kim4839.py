f = open('24-kim4839.txt').read()
k = 1
rk = 0

for i in range(1, len(f)):
    if f[i] + f[i-1] != 'PP':
        k += 1
        rk = max(k, rk)
    else:
        k = 1
print(rk)