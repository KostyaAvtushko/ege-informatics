a = '1' * 201
for i in range(201, 301):
    a = '1' * i
    while '111' in a or '222' in a:
        a = a.replace('111', '22', 1)
        a = a.replace('222', '1', 1)
    if a.count('2') == 0:
        print(i)