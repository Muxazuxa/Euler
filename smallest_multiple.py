def sm_mul():
    n = 20
    while True:
        if n % 19 == 0 and n % 18 == 0 and n % 17 == 0 and n % 16 == 0 and n % 15 == 0 \
                and n % 14 == 0 and n % 13 == 0 and n % 12 == 0 and n % 11 == 0:
            return n
        n += 20