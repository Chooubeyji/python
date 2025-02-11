#write a function that takes variable number of arguments and returns the sum of the arguments
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
# The function sum_all takes a variable number of arguments and returns the sum of the arguments.
# The function sum_all is defined with a variable-length argument list *args.
# The sum of the arguments is calculated using the sum function and returned.
# The function sum_all is called with different numbers of arguments.
# The sum of the arguments is calculated and displayed as output.
# The function sum_all can be used to calculate the sum of any number of arguments.
# The function sum_all is defined using the *args syntax to accept a variable number of arguments.

