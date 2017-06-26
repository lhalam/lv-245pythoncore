# 1
# Присвоїти цілій змінній h третю з кінця цифру в записі
# додатного цілого числа k.
# Вивести k та h.
#k = 130985
k = input('Please enter number and press "Enter": ')
if len(k) > 2:
    pass
else:
    k = input(('Please enter bigger number and press "Enter": '))
h = int(k[-3])
print('Exercise 1:')
print('The third digit at the end of the number {} is {}'\
      .format(k, h))