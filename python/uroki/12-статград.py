a = "022222222111110"
for s1 in range(0, 100):
    for s2 in range(0, 1000):
        a = '0' + s1*'1' + s2*'2' + '0'
        while '00' not in a:
            a = a.replace('021', '102', 1)
            a = a.replace('022', '301', 1)
            a = a.replace('02', '20', 1)
            a = a.replace('01', '10', 1)
        if a.count('2') > 2:
            print(s1, s2, a)
