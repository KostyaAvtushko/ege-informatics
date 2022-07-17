from statistics import mode
f = open("24-35913.txt")
rline = ""
minn = 12312321
for line in f:
    if line.count("N") < minn:
        minn = line.count("N")
        rline = line
print(mode(rline))