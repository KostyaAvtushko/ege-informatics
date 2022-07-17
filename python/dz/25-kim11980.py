for i in range(123458, 10**8):
    if i % 19 == 0:
        if str(i)[:4] == "1234" and str(i)[-2:] == "58":
            print(i, i // 19)

