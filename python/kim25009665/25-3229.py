s = "12345?6?8"
for x1 in range(0, 10):
    for x2 in range(0, 10):
        ch = "12345" + str(x1) + "6" + str(x2) + "8"
        if int(ch) % 17 == 0:
            print(ch, int(ch) // 17)
