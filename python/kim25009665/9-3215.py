f = open('9-kimdosr.txt').read()

a = f.split("\n")
k = 1

for i in a:
    if i != '':
        c = i.split("\t")
        print(c)
        ic = []
        for o in c:
            ic.append(int(o))

        a = max(ic)
        b = min(ic)
        ic.remove(a)
        ic.remove(b)
        sk = 0
        for ch in ic:
            sk += ch**2
        if (a + b)**2 >= sk:
            print(ic, a, b, (a + b) ** 2 - sk)
            k += 1

print(k)
