# exercise 1
print('exercise 1')
# create variables with them values like dictionary
# key_index starts from zero position to max_key_index include
def create_variables(var_name, max_key_index=30, var_values=None):
    var = {}
    var_keys = []
    if var_values == None:
        var_values = list(range(max_key_index + 1))
    # else var_values must contain list with values of variables
    for i in range(max_key_index + 1):
        var_key = str(var_name) + str(i)
        var_keys.append(var_key)
    for i, j in zip(var_keys, var_values):
        part_of_var = dict([(i, j)])
        var.update(part_of_var)
    return var

def numerators_calculation(variable, multiplier, max_power_index=30):
    result_variable = 0
    for (key, val), power in zip(variable.items(),
                                 list(range(max_power_index + 1))[::-1]):
        part_result_variable = (val * (multiplier ** power))
        result_variable += part_result_variable
    return result_variable

def denominator_calculation(variable, x, z, max_power_index=30):
    result_variable = 0
    for (key, val), power in zip(variable.items(),
                                 list(range(max_power_index + 1))[::-1]):
        part_result_variable = (val * (x + z) ** power)
        result_variable += part_result_variable
    return result_variable

def fraction_calculation(a, b, c, x, y, z):
    result = (((numerators_calculation(a, x) ** 2) -
               numerators_calculation(b, y))
              / denominator_calculation(c, x, z))
    return round(result, 3)
# show result
a = create_variables('a')
b = create_variables('b')
c = create_variables('c')
x, y, z = 2, 2, 2
print('result is:',
      fraction_calculation(a, b, c, x, y, z))

# exercise 2
print('\nexercise 2')
def calculate_factorial(number):
    result = 1
    if number == 0:
        result = 1
    else:
        for i in range(1, number + 1):
            result *= i
    return result

# to calculate factorial - opinion 2
# def calculate_factorial(numbers):
#     from functools import reduce
#     if numbers == 0:
#         return 1
#     else:
#         return reduce(lambda number, result=1: number * result,\
#                    [i for i in range(1, numbers + 1)])

def calculate_expression(m, n):
    result = ((calculate_factorial(n) * calculate_factorial(m)) /
              calculate_factorial(n + m))
    return result
# show result
print('result is:',
      round(calculate_expression(2, 2), 3))

# exercise 3
print('\nexercise 3:')
def review_word(x, y):
    for i in x:
        if not i in y or len(x) != len(y):
            break
        else:
            for j in y:
                if i == j:
                    if x.count(i) != y.count(j):
                        break
    else:
        return y

def perestanovka(words):
    result = []
    for i in words[1:]:
        if review_word(words[0], i):
            result.append(i)
    return ', '.join(result)

# show result
input_words = ['cat', 'alex', 'tac', 'atc', 'tca']
print('from word "{}" we can create words: {}'. \
      format(input_words[0], perestanovka(input_words)))

# exercise 4
print('\nexercise 4:')


# create matrix with random numbers
def create_matrix(max_number, row=5, col=5):
    import random
    matrix = []
    for i in range(row):
        matrix.append([])
        for j in range(col):
            matrix[i].append(random.randint(0, max_number))
    return matrix


def find_max_number_index(matrix):
    dict_max_numbers = {}
    for i in range(len(matrix)):
        row = i
        col = matrix[row].index(max(matrix[row]))
        dict_max_numbers[(row, col)] = max(matrix[row])
    for j in dict_max_numbers:
        return max((dict_max_numbers[i], i) for i in dict_max_numbers)


def change_max_elements(matrix_1, matrix_2):
    max_number_matrix_1 = find_max_number_index(matrix_1)[0]
    max_number_matrix_2 = find_max_number_index(matrix_2)[0]
    matrix_1[find_max_number_index(matrix_1)[1][0]][find_max_number_index(matrix_1)[1][1]] \
        = max_number_matrix_2
    matrix_2[find_max_number_index(matrix_2)[1][0]][find_max_number_index(matrix_2)[1][1]] \
        = max_number_matrix_1
    return 'matrix_1:\n{},\n matrix_2:\n{}'.format(matrix_1, matrix_2)


matrix_a = create_matrix(100)
matrix_b = create_matrix(100)
print('matrix a:\n{}'.format(matrix_a))
print('The max number in matrix_a and his index is {}'.format(find_max_number_index(matrix_a)))
print('matrix b:\n{}'.format(matrix_b))
print('The max number in matrix_b and his index is {}'.format(find_max_number_index(matrix_b)))
print('change max elements between matrix_a and matrix_b\n', change_max_elements(matrix_a, matrix_b))

# exercise 5
