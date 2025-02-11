#print the multiplication table of a number up to 10, but skip the fifth iteration
number = int(input("Enter a number: "))
for i in range(1, 11):
    if i == 5:
        continue
    print(number, "x", i, "=", number*i)
# if i == 5:
 #       continue  this is the code that skips the fifth iteration  
# The code above prompts the user to enter a number, which is stored in the variable number.

# The for loop iterates through each number from 1 to 10.

