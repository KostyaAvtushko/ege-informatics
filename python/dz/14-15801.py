a = 36**7 + 6**19 - 18
k = 0
while a > 0:
    if a % 6 == 5:
        k += 1
    a //= 6
print(k)
