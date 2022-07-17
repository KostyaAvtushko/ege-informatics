s = 0

def F(n):
    global s
    s += 1
    if n >= 1:
        s += 1
        F(n-1)
        F(n//3)
        s += 1
F(280)
print(s)