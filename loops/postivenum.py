# given a list of numbers return a list of positive numbers
# Number of inputs to take
n = int(input("Enter the number of elements: "))

numbers = []
for i in range(n):
    num = float(input("Enter number : "))
    numbers.append(num)

positive_numbers = 0
for num in numbers:
    if num > 0:
        positive_numbers += 1
print("Positive numbers: " , positive_numbers)    
# The code above prompts the user to enter the number of elements in the list.
# The list is stored in the variable numbers.
# The variable positive_numbers is initialized to 0.
# The for loop iterates through each number in the list.
# If the number is greater than 0, the positive_numbers variable is incremented by 1.
# Finally, the total count of positive numbers is printed.      
