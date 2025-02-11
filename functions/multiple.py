#create a function that returns both the area and circumference of a circle when the radius is given    
import math
def circle_properties(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference
radius = float(input("enter the raidus of the circle :" ))
print("The area and circumference of the circle are:", circle_properties(radius))

# The code above defines a function named circle_properties that takes the radius of a circle as an argument.
# The function calculates the area and circumference of the circle using the given radius.
# The area is calculated as πr^2, and the circumference is calculated as 2πr.
# The function returns both the area and circumference as a tuple.
# The user is prompted to enter the radius of the circle, which is stored in the variable radius.
# The function circle_properties is called with the input radius, and the area and circumference are printed.
# The area and circumference of the circle are displayed as output.
