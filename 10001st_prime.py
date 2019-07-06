def eratoshpene():
    l = list(range(1000000))
    l[1] = 0
    sum = 0
    for i in l:
        if i > 0:
            sum += 1
            if sum == 10001:
                return i
            for j in range(i+i, len(l), i):
                l[j] = 0

print(eratoshpene())