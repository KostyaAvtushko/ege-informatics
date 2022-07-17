f = open("24-polyakobV33355.txt").read()
s = f.split("\n")

kk = 0

for i in s:
    if i.count("J") > i.count("E"):
        kk += 1
print(kk)