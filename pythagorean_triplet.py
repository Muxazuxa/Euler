import math

def triplet():
    for i in range(4, 1000):
        for j in range(5, 1000):
            c = pow(i,2) + pow(j,2)
            if math.sqrt(c) - int(math.sqrt(c)) == 0:
                return str(i) + ' ' + str(j) + ' ' + str(int(math.sqrt(c)))
