f = open("C:\ege-informatics-main\python\zadanie24_2.txt").readline()

mk = 0
k = 0
for x in range(1, len(f)-1):
    if f[x] == "D":
        k += 1
        if k > mk:
            mk = k
    else:
        k = 0

print(mk)