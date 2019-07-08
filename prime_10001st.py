def eratoshpene(n):
    if n < 0:
        return 'Number must be positive'
    elif type(n) is not int:
        return 'Number must be Integer!'
    else:
        l = list(range(1000000))
        l[1] = 0
        sum = 0
        for i in l:
            if i > 0:
                sum += 1
                if sum == n:
                    return i
                for j in range(i+i, len(l), i):
                    l[j] = 0