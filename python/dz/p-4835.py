def Not(x):
    if x == 1:
        return 0
    else:
        return 1
#4835
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((w <= y) and (Not(x) <= z)) <= ((z == w) or (y and Not(x)))):
                    print(x, y, z, w)




