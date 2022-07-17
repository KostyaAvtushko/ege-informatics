a = 3*216**4 + 2*36**6 - 648
k = 0
while a > 0:
    if a % 6 == 5:
        k += 1
    a //= 6
print(k)