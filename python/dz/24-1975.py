f = open("24-1975.txt").readline()
while "PP" in f:
    f = f.replace("PP", "P P")
f = f.split()
print(len(max(f, key=len)))





