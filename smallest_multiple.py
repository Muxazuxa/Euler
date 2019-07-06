def sm_mul():
    n = 0
    for i in range(1, 1000000000):
        n += 20
        if n % 19 == 0 and n % 18 == 0 and n % 17 == 0 and n % 16 == 0 and n % 15 == 0 \
                and n % 14 == 0 and n % 13 == 0 and n % 12 == 0 and n % 11 == 0:
            return n

print(sm_mul())