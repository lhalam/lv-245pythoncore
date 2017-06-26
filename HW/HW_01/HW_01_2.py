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