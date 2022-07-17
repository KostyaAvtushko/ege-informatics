f = open("24-4528.txt").readline()
f = f.split(".")

rk = ''
for i in range(len(f)-5):
    s = f[i] + "." + f[i+1] + "." +f[i+2] + "." + f[i+3] + "." + f[i+4] + "." + f[i+5]
    rk = max(rk, s, key=len)
print(len(rk))
