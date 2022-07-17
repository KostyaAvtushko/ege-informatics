f = open('24-27699.txt').read()

k = 0
rk = 0

for i in range(0, len(f)):
    if (f[i] == "L" and k % 3 == 0) or (f[i] == "D" and k % 3 == 1) or (f[i] == "R" and k % 3 == 2):
        k += 1
        rk = max(rk, k)
    elif f[i] == "L":
        k = 1
    else:
        k = 0
print(rk)