a = 95*'1' + 31*'7'
while '1111' in a:
    a = a.replace('1111', '7', 1)
    a = a.replace('77', '1', 1)
print(a)

