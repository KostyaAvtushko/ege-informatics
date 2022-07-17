for i in range(95632, 95701):
    chdels = []
    for d in range(1, i+1):
        if d % 2 == 0 and i % d == 0:
            chdels.append(d)
        if len(chdels) > 6:
            break
    if len(chdels) == 6:
        print(chdels)