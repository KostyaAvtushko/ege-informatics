'''
    x&25 ≠ 0 → (x&17 = 0 → x&А ≠ 0)
    A(min)-?
    10 = 1010
    3  = 0011
         0010 = 2
'''
print(14&5)
print(10&3)
for a in range(0, 1000):
    ok = 1
    for x in range(0, 1000):
        if not((x & 25 !=0) <= ((x & 17 == 0) <= (x & a != 0))):
            ok = 0
    if ok == 1:
        print(a)