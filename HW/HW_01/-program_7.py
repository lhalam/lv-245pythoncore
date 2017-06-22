k = int(input('k = '))

if 0<k<366:
    i = 1
    while k % i == 0:
        print i
        i += i
