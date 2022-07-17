for i in range(312614, 312652):
    divs = []
    for d in range(1, i+1):
        if i % d == 0 and i not in divs:
            divs.append(d)
        if len(divs) > 6:
            break
    if len(divs) == 6:
        print("Число: ", i, "Делители:", divs)

