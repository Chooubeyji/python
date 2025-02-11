# factorial of a number using while loop
number = int(input("Enter a number: ")) 
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print("Factorial value is ", factorial)    
# The code above calculates the factorial of a number using a while loop.
# The user is prompted to enter a number, which is stored in the variable number.
# The variable factorial is initialized to 1.
# The while loop continues as long as the number is greater than 0.
# Inside the loop, the factorial is multiplied by the number and the number is decremented by 1.
# Finally, the factorial value is printed.
