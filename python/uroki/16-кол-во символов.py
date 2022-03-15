'''
(№ 4189) (П. Волгин) Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число, задан следующими соотношениями:
F(0) = 2
F(n) = F(n–1), при 0 < n ≤ 15
F(n) = 1,6*F(n–3), при 15 < n < 95
F(n) = 3,3*F(n–2), при n ≥ 95
Какая цифра встречается чаще всего в целой части значения функции F(33)?
'''

def F(n):
    if n == 0:
        return 2
    if n > 0 and n <= 15:
        return F(n - 1)
    if n < 95 and n > 15:
        return 1.6*F(n-3)
    if n >= 95:
        return 3.3*F(n-2)


a = 123721983694616546
s = str(a) + "odashbodbpnaspdobaspoidpaaaaaaaaaaaaa"
print(s)

b = [0]*150
print(b)

for i in range(0, len(s)):
    b[ord(s[i])] += 1
print(b)

mk = 0
ms = 0

for i in range(0, len(b)-1):
    if mk < b[i]:
        mk = b[i]
        ms = i

print(mk, ms, chr(ms))