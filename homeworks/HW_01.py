# 1
# Присвоїти цілій змінній h третю з кінця цифру в записі
# додатного цілого числа k.
# Вивести k та h.
k = 130985
h = int(str(k)[-3])
print('Exercise 1:')
print('Answers are {} = {}, {} = {}'.format('k', k, 'h', h))

# 2
# Присвоїти цілій змінній d
# першу цифру з дробової частини додатного дробового числа x.
# Вивести x та d.
x = 32.597
for i in range(len(str(x))):
    if str(x)[i] == '.':
        d = int(str(x)[i + 1])
print('\n')
print('Exercise 2:')
print('Answers are {} = {}, {} = {}'.format('x', x, 'd', d))

# 3
# Цілій змінній s
# присвоїти суму цифр трьохзначного цілого числа числа k.
# Вивести s та k.
s = 0
k = 123
for i in str(k):
    s += int(i)
print('\n')
print('Exercise 3:')
print('Answers are {} = {}, {} = {}'.format('s', s, 'k', k))

# 4
# Йде k-а секунда доби.
# Визначити, скільки повних годин (h) і повних хвилин (m)
# пройшло до цього моменту.
import copy
k = 13257
k_for_answer = copy.copy(k)
h = 0
m = 0
while k >= 3600:
    k -= 3600
    h += 1
else:
    while k >= 60:
        k -= 60
        m += 1
print('\n')
print('Exercise 4:')
print('The {0} {1} is {2} {3}, {4} {5}, and {6} {1}'.\
      format(k_for_answer, 'seconds', h, 'hours', m, 'minutes', k))

# 5
# Визначити f - кут (в градусах) між положенням годинної стрілки
# на початку доби і її положенням в h годині,
# m хвилин і s секунд.
h = 3
m = 40
s = 57
degree = (h * 30) + \
         ((m * 6) / 12) + \
         ((s * 0.1) / (12 * 60))
print('\n')
print('Exercise 5:')
print('The degree between zero {} and present positions {} is {} degrees'.\
      format('00:00:00', str(h) + ':' + str(m) + ':' + str(s), round(degree, 1)))

# 6
# Визначити h - повну кількість годин і
# m - повну кількість хвилин, які пройшли від
# початку доби до того моменту (в першій половині дня), коли годинна стрілка
# повернулась на f градусів.
input_degree = degree
h = 0
m = 0
while input_degree >= 30:
    input_degree -= 30
    h += 1
else:
    while input_degree >= (6 / 12):
        input_degree -= (6 / 12)
        m += 1
print('\n')
print('Exercise 6:')
print('The full hours and minutes after {} {} is {} {} and {} {}'.\
      format(round(degree, 1), 'degrees', h, 'hours', m, 'minutes'))

# 7
# Нехай k - ціле від 1 до 365.
# Присвоїти цілій змінній n значення 1, 2,…,6 чи 7 залежно від
# того , на який день тижня
# (понеділок, вівторок, …, суботу чи неділю)
# припадає k -й день не високосного року, в якому 1 січня - понеділок

k = 365
k_copy = k
week = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
        ]
months = {
    'January' : 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
         }

months_copy = months.copy()
for key in months.keys():
    for val in months.values():
        for i in range(1, 8):
            if k > 0 and months[key] > 0:
                answer = \
                    ("After {0} day it's {2} {1}"\
                     .format(k_copy, key, months_copy[key] + 1\
                             - months[key], i))
                months[key] -= 1
                k -= 1
n = k_copy - ((k_copy // len(week)) * len(week))

print('\n')
print('Exercise 7:')
print(answer)
print("n = {} and this is {} if year started from {}"\
              .format(n+1 if n < 1 else n, week[n], week[1]))

# 8
# Поміняти місцями значення цілих змінних
# x і y, не використовуючи додаткові змінні.
x = 'Olexandr'
y = 'Zhytenko'
print('\n')
print('Exercise 8:')
print('Before changing "{}" is {} and "{}" is {}'.format('x', x, 'y', y))

x, y = y, x

print('After changing "{}" is {} and "{}" is {}'.format('x', x, 'y', y))

# 9
# Обчислити довжину кола, площу круга і об’єм кулі
# одного і того ж заданого радіуса R
R = .15
import math
C = 2 * math.pi * R
S = math.pi * (R**2)
V = (4 / 3) * math.pi * (R**3)
print('\n')
print('Exercise 9:')
print('The length of circle with {} = {} metres \
is {}, his area is {} and volume is {}'.\
      format('R', R, round(C, 2), round(S, 2), round(V, 2)))

# 10
# Знайти добуток цифр заданого чотиризначного числа
input_number = 1984
result = 1
for number in str(input_number):
    result *= int(number)
print('\n')
print('Exercise 10:')
print('The product of numbers {} is {}'\
      .format(input_number, result))

# 11
# Визначити число,
# яке отримано виписуванням в оберненому порядку цифр заданого
# трьохзначного числа.
input_number = 123
result = ''
for number in str(input_number)[::-1]:
    result += number
print('\n')
print('Exercise 11:')
print('The result from {} is {}'\
    .format(input_number, int(result)))

# 12
# Для довільних дійсних чисел a, b, і c
# визначити, чи має рівняння ax2+bx+c=0 хоча б один
# дійсний корінь і якщо так, то видрукувати його
print('\n')
print('Exercise 12:')
a = 5
b = 12
c = 5
D = (b**2) - 4 * a * c
import math
if D > 0:
    print('There is two roots of this equation:')
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print('{0} = {2}, and {1} = {3}'\
          .format('x1', 'x2', round(x1, 2), round(x2, 2)))
elif D == 0:
    print('There only one root of this equation')
    x = - (b / (2 * a))
    print(print('The root {} = {}'.format('x1', round(x1, 2))))
else:
    print("There aren't roots of this equation")

# 13
# Визначити, чи рівна сума двох перших цифр
# заданого чотиризначного числа сумі двох
# його останніх цифр; Якщо так, то видрукувати цю суму

input_number = 8484
result = 0
print('\n')
print('Exercise 13:')
first_sum = int(str(input_number)[0]) + int(str(input_number)[1])
last_sum = int(str(input_number)[-1]) + int(str(input_number)[-2])
if first_sum == last_sum:
    result = first_sum
    print('The sum is {}'.format(result))
else:
    print('The {} = {} is not equal {} = {}'\
          .format('first_sum', first_sum, 'last_sum', last_sum))

# 14
# Визначити, чи рівний квадрат заданого трьохзначного числа
# кубу суми цифр цього числа
print('\n')
print('Exercise 14:')
input_number = 123
squre_input_number = input_number ** 2
sum_numbers = 0
cube_sum_numbers = 0
for number in str(input_number):
    sum_numbers += int(number)
cube_sum_numbers = sum_numbers ** 3
if squre_input_number == cube_sum_numbers:
    print('The square of number {} is equal cube of sum from his elements'\
          .format(input_number))
else:
    print('The square of number {} is not equal cube of sum from his elements' \
          .format(input_number))

# 15
# Визначити, чи є серед цифр заданого трьохзначного числа одинакові;
# Якщо є – видрукувати їх.
print('\n')
print('Exercise 15:')
input_number = 123
not_unique_numbers = ''
count = 0
if len(str(input_number)) == len(set(list(str(input_number)))):
    print('There is only unique numbers {}'. format(input_number))
else:
    for number in str(input_number):
        if number in not_unique_numbers:
            continue
        elif str(input_number).count(number) > 1:
            not_unique_numbers += number
            count += 1
    view_result = ''
    if len(not_unique_numbers) <= 1:
        view_result = not_unique_numbers
    else:
        for i in not_unique_numbers:
            if i is not not_unique_numbers[-1]:
                view_result += i
                view_result += ', '
            else:
                view_result += i
    print("In {} there is (are) {} not unique numbers, it's {} "\
      .format(input_number, count, view_result))

# 16
# Дано координати (як цілі від 1 до 8) двох полів шахової дошки.
# Визначити, чи може кінь за один хід перейти з одного із цих полів на інше.
print('\n')
print('Exercise 16:')
input_row = 1
input_col = 1
step_row = 2
step_col = 3

step = {'row': step_row, 'col': step_col}
possible_steps = {
    '1': {'row': input_row + 1, 'col': input_col + 2},
    '2': {'row': input_row + 2, 'col': input_col + 1},
    '3': {'row': input_row + 2, 'col': input_col - 1},
    '4': {'row': input_row + 1, 'col': input_col - 2},
    '5': {'row': input_row - 1, 'col': input_col - 2},
    '6': {'row': input_row - 2, 'col': input_col - 1},
    '7': {'row': input_row - 2, 'col': input_col + 1},
    '8': {'row': input_row - 1, 'col': input_col + 2}
                 }

for key in possible_steps.keys():
    if possible_steps[key] == step:
        print('Yes, the step from start position row = {}, col =  {} \
to end position row = {}, col =  {} is possible'\
.format(input_row, input_col, step_row, step_col))
        break
else:
    print('No, the step from start position row = {}, col =  {} \
to end position row = {}, col =  {} is impossible'\
.format(input_row, input_col, step_row, step_col))

# 17
# Знайти добуток цифр заданого натурального трьохзначного числа
input_number = 123
result = 1
for number in str(input_number):
    result *= int(number)
print('\n')
print('Exercise 17:')
print('The product of numbers {} is {}'\
      .format(input_number, result))