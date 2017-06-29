# # Home work
# # -----------------------------------------------------------
# # -----------------------------------------------------------
# # EX_1
#
# # n = int(input("n = "))
# #
# # suma = 0
# # for i in str(n):
# #     suma += int(i)
# # print(suma)
# #
# text = "sdkgns df1kngjen gk1jkdfnj gdfg 1df5665dgsf"
# #
# # for i in text:
# #     if i.isdigit():
# #         print(i)
# newText = " "
# for i in text:
#     if i != " ":
#         newText += i
# #      else:
# #         newText[]
# help(list())

word = []
num = []

text = "123 124 gjsdk jghd456 465 fjhgs djfhg jksdh fgjksh dgjkk jsdjsa dkfj sd lk"
newText = ""
L = []
for i in text:
  if  i != " ":
      newText += i
  else:
      L.append(newText)
      newText = ""
      # for i in L:
      #     if i.isdigit():
      #         num.append(int(i))
      #     else:
      #         word.append(str(i))
print (L)

word = []
num = []
for i in L:
    if i.isdigit():
        num.append(int(i))
    else:
        word.append(str(i))

print("Word: " + str(word))
print("Numbers: " + str(num))




