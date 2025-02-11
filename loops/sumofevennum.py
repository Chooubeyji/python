#calculate the sum of even numbers up to n
number = int(input("Enter a number: "))
sum = 0
for i in range(1, number+1):
    if i % 2 == 0:
        sum += i
print("Sum of even numbers: ", sum) 
# The code above calculates the sum of even numbers up to n.
# The user is prompted to enter a number, which is stored in the variable number.
# The variable sum is initialized to 0.
# The for loop iterates through each number from 1 to n.
# If the number is even (i.e., divisible by 2), it is added to the sum.
# Finally, the sum of even numbers is printed.       
