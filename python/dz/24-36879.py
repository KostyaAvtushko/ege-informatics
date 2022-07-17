f = open("24-36879.txt").read()

s = f.split("\n")

kk = 0

otv = []

for i in s:
    if i.count('G') < 25:
        sel = set()
        for l in i:
            sel.add(l)
        for a in sel:
            otv.append(i.rindex(a) - i.index(a))
print(max(otv))