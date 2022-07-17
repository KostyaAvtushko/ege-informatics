def f(x, y):
    if x == y:
        return 1
    if (x == 11) or (x == 18) or x > y:
        return 0
    if x < y:
        return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)
print(f(4, 8)*f(8, 23))