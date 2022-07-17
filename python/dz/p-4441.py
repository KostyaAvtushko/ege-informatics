def Not(x):
    if x == 1:
        return 0
    else:
        return 1
#4441
print("a b c d")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if (Not(a) <= b) and (b == Not(c)) and Not(d):
                    print(a, b, c, d)




