s = "012345678"
a = ["000", "111", "222", "333", "444", "555", "666", "777", "888"]
print(a)
k1 = 0
k = 0
for x1 in range(9):
    for x2 in range(9):
        for x3 in range(9):
            for x4 in range(9):
                for x5 in range(9):
                    for x6 in range(9):
                        for x7 in range(9):
                            word = s[x1] + s[x2] + s[x3] + s[x4] + s[x5] + s[x6] + s[x7]
                            if word[6] != "3" and word[6] != "4" and word[6] != "7":
                                # if not(s[x1] == s[x2] == s[x3]) and not(s[x2] == s[x3] == s[x4]) and not(s[x3] == s[x4] == s[x5]) and not(s[x4] == s[x5] == s[x6]) and not(s[x5] == s[x6] == s[x7]):
                                #     k += 1
                                for i in a:
                                    if word.count(i) == 0:
                                        k1 += 1

print(k, k1)