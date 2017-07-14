x = int(input("Horse`s position x = "))
y = int(input("Horse`s position y = "))


if (x in range(1,9)) and (y in range(1,9)):
    print 'Specify the coordinates in which the horse should move'
    x1 = int(input('x = '))
    y1 = int(input('y = '))
    if (x1 in range(1,9)) and (y1 in range(1,9)):
        if ((x1 == x + 2 and y1 == y +1) or (x1 == x + 2 and y1 == y - 1)
        or (x1 == x + 1 and y1 == y + 2) or (x1 == x - 1 and y1 == y + 2)
        or (x1 == x - 1 and y1 == y - 2) or (x1 == x - 2 and y1 == y - 1)
        or (x1 == x + 1 and y1 == y - 2) or (x1 == x - 2 and y1 == y + 1)):
            print 'True .You can move'
        else:
            print 'False .You can not move'
else:
    print 'Horse`s position does not exist on this chess board'