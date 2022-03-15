for n in range(100, 150):
    s = n * '1'
    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    print(n, s)