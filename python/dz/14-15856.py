a = 4**12 + 2**32 - 16
k = 0
while a > 0:
    if a % 2 == 1:
        k += 1
    a //= 2
print(k)
