f = int(input('f = '))


if 0 <= f <= 360:
    h = f // 30
    m = (f % 30) * 2
    print h,'hour and ',m,'minute'