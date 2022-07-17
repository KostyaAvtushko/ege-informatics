# Руслан составляет 6-буквенные коды из букв Р, У, С, Л, А, Н.
#  Каждую букву нужно использовать ровно один раз,
#  при этом нельзя ставить рядом две гласные. Сколько различных кодов может составить Руслан?

s = "РУСЛАН"
k = 0
for x1 in range(6):
    for x2 in range(6):
        for x3 in range(6):
            for x4 in range(6):
                for x5 in range(6):
                    for x6 in range(6):
                        v = s[x1] + s[x2] + s[x3] + s[x4] + s[x5] + s[x6]
                        if v.count("АУ") == 0 and v.count("УА") == 0:
                            if v.count("Р") == 1 and v.count("У") == 1 and v.count("С") == 1 and v.count("Л") == 1 and v.count("А") == 1 and v.count("Н") == 1:
                                k += 1
print(k)