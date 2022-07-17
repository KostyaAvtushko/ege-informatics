f = open('24-dosrok-polyakov.txt').read()

k = 0
mk = 0

for l in range(1, len(f)):
    if (f[l] + f[l-1] == 'BA') or (f[l] + f[l-1] == 'CA'):
        k += 1
        mk = max(mk, k)
    elif (f[l] + f[l-1] == 'AB') or (f[l] + f[l-1] == 'AC'):
        continue
    else:
        k = 0

print(mk)
