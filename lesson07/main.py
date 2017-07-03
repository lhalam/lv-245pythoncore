# def my_func():
#     print('temp')
#
# my_func()
# print(my_func())
#
# def my_func(a=10, b=20):
#     c = a + b
#     return c
#
# d = my_func(5, 9)
# print(d)
# print(my_func(7, 12))
# print(my_func(8))


# def divide(l, k):
#     result = []
#     for i in l:
#         if i % k == 0:
#             result.append(i)
#     return result
#
# print(divide(range(20), 3))


def fib(n):
    result = [1, 1]
    for i in range(2, n):
        result.append(
            result[i - 1] + result[i - 2]
        )
    return result[n - 1]


def fib_filter(n):
    result = []
    flag = 0
    while n > 0:
        if fib(flag) % 2 == 0:
            result.append(fib(flag))
            flag += 1
            n -= 1
        else:
            flag += 1
    return result


print(fib_filter(10))
