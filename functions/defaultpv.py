#write a function that greets the user.if no name is provided, the function should return "Hello, there". Otherwise, it should greet with a default name

def greet_user(name):
    return "hello ,"+ name + "!"
name = input("Enter your name: ")
if name == "":
    print(greet_user("there"))  
else:
    print(greet_user(name))

# The code above defines a function named greet_user that takes a name as an argument.
# The function returns a greeting message that includes the given name.
# The user is prompted to enter their name, which is stored in the variable name.
# If the user enters an empty string, the function greet_user is called with the default name "there".
# Otherwise, the function greet_user is called with the input name.
# The greeting message is displayed as output.


