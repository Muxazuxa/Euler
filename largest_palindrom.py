def palindrom():
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            m = i * j
            if str(m) == str(m)[::-1]:
                print(str(i) + '*' + str(j))
                return str(i*j)

print(palindrom())