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
# d = x - int(x) # 3.14 - 3 = 0.14
# d = int(str(d)[2]) # str(d)=>"0.14" str(d)[2]=>"1" =>1
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

# k = input("Введіть число k, довжиною 3 символи - ")
#
# k = str(k[-1])
# k= int(k)
# print(k)


import math
x = 3.14

print(math.modf(x)[0])












