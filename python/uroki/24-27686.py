'''
Текстовый файл состоит не более чем из 106 символов X, Y и Z.
Определите длину самой длинной последовательности,
состоящей из символов X. Хотя бы один символ X находится в последовательности.
'''

f = open("24-27686.txt")

s = f.readline()

kt = 1
mt = 0
#s = "xyxyxyxyxyyxxyxyxxxxxzxzxzzzzzxzxzxzxzxzxzx"

for i in range(1, len(s)):
    if s[i] == s[i-1] and s[i] == "X":
        kt += 1
        if mt < kt:
            mt = kt
    else:
        kt = 1

print(mt)