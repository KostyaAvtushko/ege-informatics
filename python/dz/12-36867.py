for x in range(1, 50):
    for y in range(1, 50):
        for z in range(1, 50):
            s = '0' + x*'1' + y*'2' + z*'3' + '0'
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '320', 1)
                s = s.replace('03', '3012', 1)
            if s.count('1') == 26 and s.count('2') == 54 and s.count('3') == 48:
                print(x, y, z, x+y+z+2)