a = 4*625**9 - 25**15 + 2*5**11 - 7
k = 0
while a > 0:
    if a % 5 == 4:
        k += 1
    a //= 5
print(k)