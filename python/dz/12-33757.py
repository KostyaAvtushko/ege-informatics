for x in range(1, 70):
    for y in range(1, 20):
        for z in range(1, 20):
            s = '0' + x*'1' + y*'2' + z*'3'
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '101', 1)
                s = s.replace('03', '202', 1)
            if s.count('1') == 20 and s.count('2') == 10 and s.count('3') == 70:
                print(x, y, z, s)
