def Not(x):
    if x == 1:
        return 0
    else:
        return 1
#4834
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((z <= y) and (Not(x) <= w)) <= ((z == w) or (y and Not(x)))):
                    print(x, y, z, w)




