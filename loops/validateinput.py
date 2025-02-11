#keep asking the user to enter a string until they enter a number between 1 and 10
while True:
    string = input("Enter a string: ")
    if string.isdigit():
        number = int(string)
        if number >= 1 and number <= 10:
            print("You entered a valid number.")
            break
    print("Invalid input. Please enter a number between 1 and 10.")

# The code above prompts the user to enter a string and stores it in the variable string.
# The input is checked using the isdigit method to determine if it is a number.
# If the input is a number, it is converted to an integer and stored in the variable number.
# The number is then checked to see if it is between 1 and 10.
# If the number is valid, a message is printed, and the loop is broken to exit the loop.
# If the input is not a valid number, an error message is printed, and the loop continues to prompt the user for input.
# This process continues until the user enters a valid number between 1 and 10.
# Note that the isdigit method is used to check if the input is a number.