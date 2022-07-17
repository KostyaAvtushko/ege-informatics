s = ['С', 'А', 'Л', 'Ь']
k = 0
for a1 in s:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                for a5 in s:
                    for a6 in s:
                        v = a1 + a2 + a3 + a4 + a5 + a6
                        if v.count('A') <= 1:
                            k += 1
print(k)