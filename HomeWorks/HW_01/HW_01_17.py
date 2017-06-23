a = 456
my_sum = 1
while a:
    print "a:", a,
    d = a%10
    print "d:",d,
    my_sum *= d
    a = a/10
    print " => a:", a
print "my_sum:", my_sum