#check a number is prime or not
number = int(input("Enter a number: "))
is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
print("Is the number prime?", is_prime)        

# The code above prompts the user to enter a number and stores it in the variable number.
# The variable is_prime is initialized to True, assuming the number is prime initially.
# If the number is less than 2, it is not considered prime, and the is_prime variable is set to False.
# Otherwise, a for loop is used to iterate through numbers from 2 to number
# Inside the loop, the number is divided by the current value of i.
# If the remainder is 0, it means the number is divisible by i, and hence not prime.
# The is_prime variable is set to False, and the loop is broken to exit the loop.
# Finally, the result is printed to indicate whether the number is prime or not.