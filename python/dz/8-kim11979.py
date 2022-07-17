k = 0
for x1 in "ВИШНЯ":
    for x2 in "ВИШНЯ":
        for x3 in "ВИШНЯ":
            for x4 in "ВИШНЯ":
                for x5 in "ВИШНЯ":
                    for x6 in "ВИШНЯ":
                        word = x1 + x2 + x3 + x4 + x5 + x6
                        if word.count("В") <= 1 and word[0] != "Ш" and word[5] != "И" and word[5] != "Я":
                            k += 1
print(k)