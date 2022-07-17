s = "ЧОАНИМЕ"
k = 0
for x1 in range(7):
    for x2 in range(7):
        for x3 in range(7):
            for x4 in range(7):
                word = s[x1] + s[x2] + s[x3] + s[x4]
                if word.count("М") == 3:
                    k += 1
for y1 in range(7):
    for y2 in range(7):
        for y3 in range(7):
            for y4 in range(7):
                for y5 in range(7):
                    word = s[y1] + s[y2] + s[y3] + s[y4] + s[y5]
                    if word.count("М") == 3:
                        k += 1
for z1 in range(7):
    for z2 in range(7):
        for z3 in range(7):
            for z4 in range(7):
                for z5 in range(7):
                    for z6 in range(7):
                        word = s[z1] + s[z2] + s[z3] + s[z4] + s[z5] + s[z6]
                        if word.count("М") == 3:
                            k += 1
print(k)