def F(a, b):
    if a == 0:
        return b
    if a > 0:
        return F(a // 10, 10*b + (a % 10))

print(F(3421872931, 0))

# for i in range(300000, 4000000000):
#     if F(i, 0) > 1392781242:
#         print(i, F(i, 0))
