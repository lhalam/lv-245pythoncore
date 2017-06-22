# -*- coding: utf-8 -*-

# start = 0
# end = 5
# while start < end:
#     start += 1
#     print "bef: ",  start
#     if not start %2:
#         continue
#     print "aft:",  start
# else:
#     print " ELSE: ", start
# start = 0
# end = 5
# while start < end:
#     start += 1
#     print "bef: ",  start
#     if not start %2:
#         break
#     print "aft:",  start
# else:
#     print "else:", start
# print "END"

# st = "abcde"
# while st:
#     print st
#     st = st[:-1]

# print range(10)
# print range(5, 10)
# print range(-10, -5)
# print range(1, 10, 2)
# print range(50, 10, -2)

# for i in range(5):
#     print i

# st = "abcde"
# for i in st:
#     print i
# for i in range(len(st)):
#     print i , st[i]


# n = 4565676
# my_sum = 0
# while n:
#     print "n:", n,
#     d = n%10
#     print "d:",d, 
#     my_sum += d
#     n = n/10
#     print " => n:", n
# print "my_sum:", my_sum

n = 987654321
my_sum = 0
for i in str(n):
    # my_sum += int(i)
    my_sum = my_sum + int(i)
print my_sum
# print sum(int(i) for i in str(n))     

st = "vdashgv127382hcdasj76`183bcvdjsvfbsj2169"
# 127382
# 76
# 183
# 2169
a = "a0123456789b"
# print dir(a)
for i in a:
    print i,  "0" <= i <= "9"
    print i , i.isdigit()

print "3215634".isdigit()