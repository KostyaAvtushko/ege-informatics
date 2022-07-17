f = open("24-4217.txt").readline()
f = f.split('QW')

rk = ''
for i in range(len(f)):
    rk = max(rk, f[i], key=len)
print(len(rk)+2, rk)#по краям можем добавить W и Q
