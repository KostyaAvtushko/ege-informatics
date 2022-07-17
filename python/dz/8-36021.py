s = "ВИШНЯ"
k = 0
for x1 in range(5):
    for x2 in range(5):
        for x3 in range(5):
            for x4 in range(5):
                for x5 in range(5):
                    for x6 in range(5):
                        word = s[x1] + s[x2] + s[x3] + s[x4] + s[x5] + s[x6]
                        if word[0] != "Ш" and word[5] != "И" and word[5] != "Я" and word.count("B") <= 1:
                            k += 1
print(k)