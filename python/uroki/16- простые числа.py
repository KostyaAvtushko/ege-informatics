'''
(№ 4883) (П. Волгин) Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число,
 задан следующими соотношениями:
F(n) = 1 при n = 0
F(n) = 7·(n - 1) + F(n - 1) при n > 0
Сколько существует значений n на отрезке [2, 200], для которых значение функции F(n) является простым числом?
'''
def isSimple(p):
    res = True
    d = 2
    if p % d == 0:
        return p == 2
    d = 3
    while d <= int(p**0.5):
        if p % d == 0:
            res = False
            break
        d += 2
    return res

def F(n):
    if n == 0:
        return 1
    if n > 0:
        return 7*(n - 1) + F(n - 1)

k = 0
for i in range(2, 201):
    if isSimple(F(i)):
        k += 1

print(k)