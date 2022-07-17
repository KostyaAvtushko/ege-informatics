s = '2'* 282
while '222' in s or '666' in s:
    if '222' in s:
        s = s.replace('222', '6', 1)
    else:
        s = s.replace('6666', '2', 1)