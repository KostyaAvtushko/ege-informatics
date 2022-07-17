dels = []
for i in range(210235, 210300):
    td = []
    for dl in range(2, int(i/2 + 1)):
        if i % dl == 0:
            td.append(dl)
    if len(td) == 4:
        for j in td:
            dels.append(j)
print(dels)