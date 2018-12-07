for i in range(100, 1000):
    temp = list(str(i))
    a = temp[0]
    b = temp[1]
    c = temp[2]

    if int(a)**3 + int(b)**3 + int(c)**3 == i:
        print(i)