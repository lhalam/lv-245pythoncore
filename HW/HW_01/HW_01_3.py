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
