chs = []
maxdels = []

for i in range(289123456, 389123456):
    ndels = []
    for d in range(2, int(i**0.5)):
        if i % d == 0:
            ndels.append(d)
        if len(ndels) > 3:
            break
    if len(ndels) == 3:
        maxdels.append(max(ndels))
        chs.append(i)
print(chs)
print(ndels)