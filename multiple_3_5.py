def multiple_3_5(n):
    if n <= 3:
        return 'Number must be greater 3'
    elif type(n)  is not int:
        return 'Number must be Integer!'
    else:
        sum = 0
        for i in range(1, n):
            if i % 3 == 0:
                sum += i
            elif i % 5 == 0:
                sum += i
        return sum
