Count = [10]
def my_print(fun, *arg, **qwarg):
    print "start {}".format(Count[0])
    print arg
    print qwarg
    print fun
    Count[0] = Count[0] + 1

    return fun

@my_print
@my_print
def my_sum(a=1, b=1):
    return a+b

print my_sum(5 ,a=10)
# print my_print2(my_print1(my_sum))

# @my_print
# def my_div(a=1, b=1):
#     return a/b
print my_sum

print my_sum()

# print my_div()