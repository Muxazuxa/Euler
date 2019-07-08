def sum_diff(n):
    if n < 0:
        return 'Number must be positive'
    elif type(n) is not int:
        return 'Number must be Integer!'
    else:
        sum1 = 0
        sum2 = 0
        for i in range(1, n+1):
            sum1 += i*i
            sum2 += i
        return sum2*sum2-sum1

