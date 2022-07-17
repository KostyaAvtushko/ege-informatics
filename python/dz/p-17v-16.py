def F(n):
    if n < 2:
        return n
    if n >= 2 and n % 2 == 0:
        return F(n / 2) + 1
    if n >= 2 and n % 2 != 0:
        return F(3 * n + 1) + 1
k = 0
for i in range(1, 101):
    if F(i) > 100:
        k += 1
print(k)