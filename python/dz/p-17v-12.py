a = 107*'X'
while ('XXX' in a) or ('ZYX' in a) or ('ZXX' in a):
    a = a.replace('XXX', 'ZZ', 1)
    a = a.replace('ZYX', 'X', 1)
    a = a.replace('ZXX', 'Y', 1)
print(a)