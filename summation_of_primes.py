def summ_primes(n):
    l = list(range(n+1))
    l[1] = 0
    sum = 0
    for i in l:
        if i > 0:
            sum += i
            for j in range(i+i, len(l), i):
                l[j] = 0
    return sum

print(summ_primes(2000000))
