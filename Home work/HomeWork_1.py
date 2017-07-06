# Home work
# -----------------------------------------------------------
# -----------------------------------------------------------

# # EX_1
# from builtins import input
#
# k = int(input("Присвойте значення змінній - k: "))
#
# if len(str(k)) > 2:
#     if k < 0:
#         print("Введене число відємне, ще раз повторіть операцію!!!")
#     else:
#         k = str(k)
#         print (str("h = ") + k[-3])
#         print (str("k = ") + k)
# else:
#     print("Число - " + str(k) + " занадто коротке!!!")

# EX_2
# import math
# x = float(input("Присвойте значення змінній - x: "))
# x = 3.14
# d = x - int(x)

# print(math.modf(x))
# print("Число 'd' = " + str(d))

# EX_3

# k = input("Введіть ціле число, довжиною 3 символи - ")
#
# if 2 < len(str(k)) < 4:
#     k = str(k)
#     k1 = k[0]
#     k2 = k[1]
#     k3 = k[2]
#
#     s = int(k1) + int(k2) + int(k3)
#
#     print("Число 's' = " + str(s))
#     print("Число 'k' = " + str(k))
# else:
#     print("Число має більше або менше 3 символів")

# EX_4
#
# k = int(input("Введіть кількість секунд - "))
#
# if k > 0:
#     h = int(k/3600)
#     m = int((k - h*3600)/60)
#     print("Поточний час - " + str(h)+ ":" + str(m))
# else:
#     print("Кількість секунд не може бути відємною")

# # EX_5
#
# h = int(input('години = '))
# m = int(input('хвилини = '))
# s = int(input('секунди = '))
#
# if (0 <= h <= 11) and (0 <= m <= 59) and (0 <= s <= 59 ):
#     h1 = h * (360/12)
#     m1 = m * (360/12/60)
#     s1 = s * (360/12/60/60)
#
#     time_gradus = h1 + m1 + s1
#     print('%.2f' % time_gradus)

# # EX_6
#
# gradus = float(input('Градуси = '))
#
# if (0 <= gradus <= 360):
#     h = gradus // (360/12)
#     m = (gradus % (360/12)) * 2
#
# print(h,':',m)

# EX_7
#
# days = []
# for k in range(365):
#     if k != 0:
#         if   (k % 7) == 1: day = "пн_"  + str(k)
#         elif (k % 7) == 2: day = "вт_"  + str(k)
#         elif (k % 7) == 3: day = "сер_" + str(k)
#         elif (k % 7) == 4: day = "чт_"  + str(k)
#         elif (k % 7) == 5: day = "пт_"  + str(k)
#         elif (k % 7) == 6: day = "сб_"  + str(k)
#         elif (k % 7) == 0: day = "нд_"  + str(k)
#         days.append(day)
#
# print(days)
#
# n = int(input('день року = '))
# n -= 1
# print(days[n])


# EX_8
#
# x = int(input("Введіть змінну х - "))
# y = int(input("Введіть змінну y - "))
#
# # 2 Варіант
# # x = x + y
# # y = y - x
# # y = -y
# # x = x - y
#
# # 1 Варіант
# x,y = y,x
#
# print("x, y = " + str(x) + ", " + str(y))

# # EX_9
#
# R = float(input("Задайте радіус R кола: "))
# import math
#
# print("Довжина кола = : %.2f" % (math.pi*R*2))
# print("Площа круга  = : %.2f" % (math.pi*R**2))
# print("Об’єм кулі   = : %.2f" % (4/3*math.pi*R**3))

#
# # EX_10
#
# k = input("Введіть число k, довжиною 4 символи - ")
# k = str(k)
#
# if k.find("."):
#     k = k.replace(".","")
#
#     if 3 < len(str(k)) < 5:
#         k = str(k)
#         k1 = k[0]
#         k2 = k[1]
#         k3 = k[2]
#         k4 = k[3]
#
#         s = int(k1) * int(k2) * int(k3) * int(k4)
#
#         print("Число 's' = " + str(s))
#         print("Число 'k' = " + str(k))
#     else:
#         print("Число має більше або менше 4 символів")

# EX_11
#
# k = input("Введіть число k, довжиною 3 символи - ")
# k = str(k[::-1])
# k = int(k)
# print(k)


# # EX_12
#
# a = float(input("a: "))
# b = float(input("b: "))
# c = float(input("c: "))
#
# D = b**2 - 4*a*c
#
# if D > 0:
#     x1 = (-b+D**0.5)/2*a
#     x2 = (-b-D**0.5)/2*a
#     print(x1)
#     print(x2)
# elif D < 0:
#     print("Коренів не має")
# elif D == 0:
#     x1 = -b/2*a
#     print(x1)
#
# print(D)
#
# # EX_13
#
# k = input("Введіть число k, довжиною 4 символи - ")
# k = str(k)
#
# if k.find("."):
#     k = k.replace(".","")
#
#     if 3 < len(str(k)) < 5:
#         k = str(k)
#         k1 = k[0]
#         k2 = k[1]
#         k3 = k[2]
#         k4 = k[3]
#
#         s1 = int(k1) + int(k2)
#         s2 = int(k3) + int(k4)
#
#         if s1 == s2:
#             print("Сума перших та останніх чисел є рівною 's' = " + str(s1))
#         else:
#             print(s1,s2)
#     else:
#         print("Число має більше або менше 4 символів")

# # EX_14
#
# k = input("Введіть ціле число, довжиною 3 символи - ")
#
# if 2 < len(str(k)) < 4:
#     k = str(k)
#     k1 = k[0]
#     k2 = k[1]
#     k3 = k[2]
#
#     s1 = (int(k1) + int(k2) + int(k3))**3
#     s2 = int(k)**2
#
#     if s1 == s2:
#         print("Сума та квадрат 's1 = s2' = " + str(s1))
#     else:
#         print(s1,s2)
# else:
#     print("Число має більше або менше 3 символів")


# # EX_15
#
# k = input("Введіть ціле число, довжиною 3 символи - ")
#
# if 2 < len(str(k)) < 4:
#     k = str(k)
#     k1 = k[0]
#     k2 = k[1]
#     k3 = k[2]
#
#     if int(k1) == int(k2):
#         print(k1, k2)
#     elif int (k2) == int(k3):
#         print(k2, k3)
#     elif int(k1) == int(k3):
#         print(k1, k3)
#
# else:
#     print("Число має більше або менше 3 символів")

# # EX_17
#
#
# k = input("Введіть ціле натуральне число, довжиною 3 символи - ")
#
# if 2 < len(str(k)) < 4 and int(k) > 0 :
#     k = str(k)
#     k1 = k[0]
#     k2 = k[1]
#     k3 = k[2]
#
#     s = int(k1) * int(k2) * int(k3)
#
#     print(s)
# else:
#     print("Число не підходить за умовою")






