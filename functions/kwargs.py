#create a function that accepts any number of keyword arguments and prints them in a format
def print_all(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
print_all(name='John', age=25, city='New York')
print_all(name='Jane', age=22, city='San Francisco', country='USA')
print_all(name='Tom', age=30)
# The function print_all accepts any number of keyword arguments and prints them in a specified format.
# The function print_all is defined with a variable-length keyword argument list **kwargs.
# The keyword arguments are printed using a for loop that iterates over the items in the kwargs dictionary.
# The key and value of each keyword argument are printed using the print function.
# The function print_all is called with different keyword arguments.
# The keyword arguments are printed in the specified format.
# The function print_all can be used to print any number of keyword arguments.
# The function print_all is defined using the **kwargs syntax to accept a variable number of keyword arguments.
# The keyword arguments are stored in a dictionary and can be accessed using the items method.        
