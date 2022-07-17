f = open('27-28128.txt')
n = int(f.readline())
s = [int(i) for i in f]

mk3 = 0
mk3_2 = 0
mk3_ost1 = 0
mk3_ost2 = 0
for i in range(n):
    if s[i] % 3 == 0:
        if s[i] > mk3:
            mk3 = s[i]
        elif mk3_2 < s[i] < mk3:
            mk_2 = s[i]
    if s[i] % 3 == 1:
        mk3_ost1 = max(s[i], mk3_ost1)
    if s[i] % 3 == 2:
        mk3_ost2 = max(s[i], mk3_ost2)
print(mk3_ost1+mk3_ost2)
