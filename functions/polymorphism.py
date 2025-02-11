#write a function multiply that multiplies two numbers, but can also accept and multiply strins
def multiply(a, b):
    return a * b
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("The product is:", multiply(num1, num2))
print("The product is:", multiply("Hello ", 3))
print("The product is:", multiply(3, "Hello "))
# The code above defines a function named multiply that takes two arguments a and b.
# The function returns the product of the two input numbers.
# The user is prompted to enter two numbers, which are stored in the variables num1 and num2.
# The function multiply is called with the input numbers, and the result is printed.
# The product of the two numbers is displayed as output.
# The function multiply can also accept and multiply strings.
# The function is called with a string and an integer, and the result is printed.
# The string is repeated three times as output.
# The function is called with an integer and a string, and the result is printed.
# The string is repeated three times as output.
# The function can handle different types of input arguments and perform the multiplication accordingly.
# This is an example of polymorphism in Python, where the same function can operate on different types of data.
