s = "НИКОЛАЙ"
k = 0
for x1 in range(7):
    for x2 in range(7):
        for x3 in range(7):
            for x4 in range(7):
                v = s[x1] + s[x2] + s[x3] + s[x4]
                if v[0] != "Й" and ((v.count("А") + v.count("О") + v.count("И")) >= 1):
                    k += 1
print(k)