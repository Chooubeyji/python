#reverse a string using loops
string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string    

print("Reversed string:", reversed_string)   
# The code above reverses a string using a for loop.
# The user is prompted to enter a string, which is stored in the variable string.
# The variable reversed_string is initialized to an empty string.
# The for loop iterates through each character in the string.
# Inside the loop, each character is concatenated to the beginning of the reversed_string.
# Finally, the reversed string is printed. 
