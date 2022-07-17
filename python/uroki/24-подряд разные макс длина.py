'''
Текстовый файл состоит не более чем из 106 символов X, Y и Z.
Определите максимальное количество идущих подряд символов,
среди которых каждые два соседних различны.
'''

f = open("24-27421.txt")

s = f.readline()

kt = 1
mt = 0
#s = "xyxyxyxyxyyxxyxyxxxxxzxzxzzzzzxzxzxzxzxzxzx"

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        kt += 1
        if mt < kt:
            mt = kt
    else:
        kt = 1

print(mt)