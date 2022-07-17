s = "ГЕПАРД"
k = 0
for x1 in range(6):
    for x2 in range(6):
        for x3 in range(6):
            for x4 in range(6):
                for x5 in range(6):
                    word = s[x1] + s[x2] + s[x3] + s[x4] + s[x5]
                    if word.count("Г") == 1 and word[0] != "А" and word[4] != "Е":
                        k += 1
print(k)