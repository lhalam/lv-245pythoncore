# python
# # # n = int(input("n = "))
# # #
# # # suma = 0
# # # for i in str(n):
# # #     suma += int(i)
# # # print(suma)
# # #
# # text = "sdkgns df1kngjen gk1jkdfnj gdfg 1df5665dgsf"
# # #
# # # for i in text:
# # #     if i.isdigit():
# # #         print(i)
# # newText = " "
# # for i in text:
# #     if i != " ":
# #         newText += i
# # #      else:
# # #         newText[]
# # help(list())
#
# word = []
# num = []
#
# text = "123 124 gjsdk jghd456 465 fjhgs djfhg jksdh fgjksh dgjkk jsdjsa dkfj sd lk"
# newText = ""
# L = []
# for i in text:
#   if  i != " ":
#       newText += i
#   else:
#       L.append(newText)
#       newText = ""
#       # for i in L:
#       #     if i.isdigit():
#       #         num.append(int(i))
#       #     else:
#       #         word.append(str(i))
# print (L)
#
# word = []
# num = []
# for i in L:
#     if i.isdigit():
#         num.append(int(i))
#     else:
#         word.append(str(i))
#
# print("Word: " + str(word))
# print("Numbers: " + str(num))

#
# def my_func(b, a):
#     result = []
#     for i in range(len(a)):
#         if a[i]%b == 0:
#             result.append(a[i])
#     return result
#
# t = my_func(2,[1,1,2,3,4,5,6,7,8, 2, 4])
# print (t)

import math
def fib(n):
    List_Fibanachi = []
    i = 1
    while True:
        SQRT5 = math.sqrt(5)
        PHI = (SQRT5 + 1) / 2
        k = int(PHI ** i / SQRT5 + 0.5)
        if str(k).find("0") != -1:
            List_Fibanachi.append(k)
        if len(List_Fibanachi) == n:
            break
        i += 1
    return print(List_Fibanachi)

t = fib(10)

