# string = 'a bb ccc dddd eeeee 123 a2a2a2 456abc'
# word = ''
# result = []
# for i in string:
#     if i != ' ':
#         word += i
#     else:
#         result.append(word)
#         word = ''
# result.append(word)
# print(result)
string = 'a bb ccc dddd eeeee 123 456 abc'
words, numbers = [], []
word, number = '', ''
for i in string:
    if i != ' ' and i.isdigit():
        number += i
    else:
        numbers.append(number)
        number = ''
numbers.append(number)
numbers = [int(i) for i in numbers if i != '']
for i in string:
    if i != ' ' and i.isalpha():
        word += i
    else:
        words.append(word)
        word = ''
words.append(word)
words = [i for i in words if i != '']
print(numbers)
print(words)




