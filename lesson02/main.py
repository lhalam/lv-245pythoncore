# a = None
# if a:
#     print(True)
# else:
#     print(False)

# a = 2**20
# b = 2**20
#
# print(a is b)
#
# class A():
#     pass
#
# a1 = A()
# a2 = A()
# a3 = a1
# print(a1, a2, a3)
# print(a1 is a2)



# a = 'atr'
#
# if a:
#     print(a)
# elif not a:
#     print(None)
# i = 14
# if i > 10:
#     print('i > 10')
# elif i > 5:
#     print('5 > i < 10')
# elif i >= 0:
#     print('0 >= i < 5')
# else:
#     print('i < 0', i)

# i = 15
# temp = True if 0 < i < 10 else False
# print(temp)

#exersice_1
str1 = 'gitaddcommogitstatus'
str2 = 'git'

if str2 not in str1:
    print("In str1 there isn't substring str2")
else:
    print("The string str1 substring is {} times".format(str1.count(str2)))

#exersice_2
year = 2000
if (year % 4 and year % 100) == 0 and (year % 400 != 0):
    print("The year {} is a leap year".format(year))
else:
    print("The year {} isn't a leap year".format(year))

#exersice_3
year = 2017
month = 61
day = 191
condition_year = len(str(year)) == 4
condition_month = 0 < month <= 12
condition_day = 0 < day <= 31
if condition_year and condition_month and condition_day:
    print("The input data type - {}, {}, and {} is entered correctly".format('day', 'month', 'year'))
if not(condition_year):
    print("The input data type - {} {} is incorrect".format('year', year))
if not(condition_month):
    print("The input data type - {} {} is incorrect".format('month', month))
if not(condition_day):
    print("The input data type - {} {} is incorrect".format('day', day))


#exersise_4
a = 5
b = 12
c = 5
D = (b**2) - 4 * a * c
import math
if D > 0:
    print('There is two roots of this equation:')
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print('The roots {0} = {2}, and {1} = {3}'.format('x1', 'x2', x1, x2))
elif D == 0:
    print('There only one root of this equation')
    x = - (b / (2 * a))
    print(print('The root {} = {}'.format('x1', x1)))
else:
    print("There aren't roots of this equation")

#exersise_5
str1 = 'aaaaaagitaddcommogitstatus'
count_letters = []
for i in str1:
    count_letters.append(str1.count(i))

print(count_letters)
print(count_letters.index(max(count_letters)))
print(str1[count_letters.index(max(count_letters))])

t = { i: str1.count(i) for i in set(str1)}
print (t)
print ("max: ", max(t, key=t.get))

