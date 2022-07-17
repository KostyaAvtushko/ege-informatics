a = "12345?6?8"
for x in range(0, 10):
    for y in range(0, 10):
        a = "12345" + str(x) + "6" + str(y) + "8"
        if int(a) % 17 == 0:
            print(a, int(a) // 17)