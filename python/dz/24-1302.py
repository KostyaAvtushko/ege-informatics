f = open("24-1302.txt").readline()
f = f.replace("XZZY", "XZZ ZZY").split()
print(len(max(f, key=len)))







