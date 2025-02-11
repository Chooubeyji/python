#create an electric car class that inherits from the car class and has an additional attribute battery
#add a method to the car class that displays the full name of the car(brand and model)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f'{self.brand} {self.model}'

class ElectricCar(Car):
     def __init__(self,brand,model,battery):
         super().__init__(brand,model)
         self.battery = battery

my_tesala = ElectricCar('Tesla','Model S','100kWh')
print(my_tesala.brand)

my_car = Car('Toyota', 'Corolla')
print(my_car.brand)        
print(my_car.model)
print(my_car.full_name())
# The code above defines a Car class with two attributes: brand and model.
#init is a special method that initializes the attributes of the class.
#The __init__ method takes two arguments: brand and model.
#The self parameter refers to the current instance of the class.
#The code then creates an instance of the Car class with the brand 'Toyota' and model 'Corolla'.
#Finally, the code prints the brand and model of the car instance.
#The code then defines an ElectricCar class that inherits from the Car class.
#The ElectricCar class has an additional attribute battery.
#The __init__ method of the ElectricCar class takes three
#arguments: brand, model, and battery.
#The super() function is used to call the __init__ method of the parent class (Car).
#The code then creates an instance of the ElectricCar class with the brand 'Tesla', model 'Model S', and battery '100kWh'.
#Finally, the code prints the brand of the electric car instance.

# 