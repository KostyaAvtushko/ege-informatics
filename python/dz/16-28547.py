def F(n):
    print(n)
    if n >= 5:
        F(n - 1)
    if n > 3:
        F(n // 2)

print(F(8))