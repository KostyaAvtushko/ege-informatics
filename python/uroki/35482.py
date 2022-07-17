f = open("24-35482.txt").read()

s = f.split("\n")

rs = ""
gc = 100

mc = ""
mk = 0

for i in s:
    k = i.count("G")
    if k < gc:
        rs = i
        gc = k

seen = ""

for c in rs:
    if c not in seen:
        if rs.count(c) > mk:
            mk = rs.count(c)
            mc = c
        seen += c

print(mc)