def f(x, y):
    if x == y:
        return 1
    if x < y:
        return 0
    if x > y:
        return f(x - 5, y) + f(x - 2, y)
print(f(23, 2))