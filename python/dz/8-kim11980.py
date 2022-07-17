s = "АЕПСТУХ"
k = 0
a = 0
for x1 in range(7):
    for x2 in range(7):
        for x3 in range(7):
            for x4 in range(7):
                word = s[x1] + s[x2] + s[x3] + s[x4]
                k += 1
                if k > 1000 and word[0] != word[1] and word[1] != word[2] and word[2] != word[3]:
                    a += 1
                    print(word, k)
print(a)