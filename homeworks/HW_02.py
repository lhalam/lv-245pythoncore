# exercise 1

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
print('result of exercise 1 is:',
      fraction_calculation(a, b, c, x, y, z))

# exercise 2
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
print('result of exercise 2 is:',
      round(calculate_expression(2, 2), 3))

# exercise 3
