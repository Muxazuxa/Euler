def fibonacci_even_sum(n):
    if n < 0:
        return 'Number must be positive'
    elif type(n) is not int:
        return 'Number must be Integer!'
    else:
        a = [0,1]
        summ = 0
        while a[-1] <= n:
            b = a[-1] + a[-2]
            a.append(b)
            if b % 2 == 0:
                summ += b
        return summ
