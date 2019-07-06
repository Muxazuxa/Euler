a = [0,1]
ev_sum = 0
b = 0
while True:
    b = a[-2] + a[-1]
    if b >= 4000000:
        break
    a.append(b)
    if b % 2 == 0:
        ev_sum += b
    print(b)

print("Summ of all even numbers is: " + str(ev_sum))