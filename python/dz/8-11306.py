s = "БРОНХИ"
k = 0
for x1 in range(6):
    for x2 in range(6):
        for x3 in range(6):
            for x4 in range(6):
                word = s[x1] + s[x2] + s[x3] + s[x4]
                if word.count("Х") == 1:
                    k += 1
print(k)