# ДЕЛ(A, 40) ∧ (ДЕЛ(780, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(180, x)))
# A(мин) - ?
for a in range(1, 780):
    ok = 1
    for x in range(1, 1000):
        if not((a % 40 == 0) and ((x % 780 == 0) <= ((a % x != 0) <= (180 % x != 0)))):
            ok = 0
    if ok == 1:
        print(a)