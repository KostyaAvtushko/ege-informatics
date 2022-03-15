a = 16**2016 + 4**2015 - 64
k = 0
while a > 0:
    if a % 4 == 3:
        k += 1
    a //= 4
print(k)

