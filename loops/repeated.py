# find the first non repeated character in a string
# using loops
string = input("Enter a string: ")

for char in string:
    print(char)
    if string.count(char) == 1:
        
        print("First non repeated character is:", char)
        break

# The code above finds the first non-repeated character in a string using a for loop.
# The user is prompted to enter a string, which is stored in the variable string.
# The for loop iterates through each character in the string.
# Inside the loop, the count of the character in the string is checked.
# If the count is 1, it means the character is not repeated, and it is printed as the first non-repeated character.
# The loop is then broken to stop further iterations.
# Note that the count method is used to count the occurrences of a character in the string.


