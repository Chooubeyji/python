#create a car class with attributes like brand and model . Then create an instance of the class 
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
my_car = Car('Toyota', 'Corolla')
print(my_car.brand)        
print(my_car.model)
# The code above defines a Car class with two attributes: brand and model.
#init is a special method that initializes the attributes of the class.
#The __init__ method takes two arguments: brand and model.
#The self parameter refers to the current instance of the class.
#The code then creates an instance of the Car class with the brand 'Toyota' and model 'Corolla'.
#Finally, the code prints the brand and model of the car instance.
