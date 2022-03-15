# ¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 4))
for a in range(1, 1000):
    ok = 1
    for x in range(1, 1000):
        if not((x % a != 0) <= ((x % 6 == 0) <= (x % 4 != 0))):
            ok = 0
    if ok == 1:
        print(a)