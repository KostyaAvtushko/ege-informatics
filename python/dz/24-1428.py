f = open("24-1428.txt").readline()
f = f.replace("XY", "X Y").replace("XZ", "X Z").split()
print(len(max(f, key=len)))





