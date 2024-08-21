"""Creating a Car class with methods and instances"""

# Define the Car class
class Car:
    """Creating a Car class with 6 parameters and instances"""
    def __init__(self, make, model, body, engine, year, color, num_cupholders):
        self.make = make
        self.model = model
        self.body = body
        self.engine = engine
        self.year = year
        self.color = color
        self.num_cupholders = num_cupholders

# Prompt the user to enter the information for the car for each parameter.
# Hint: Make sure the year is an integer.
make = input("Enter your car make: ")
model = input("Enter your car model: ")
body = input("Enter your car body: ")
engine = input("Enter your car engine: ")
year = int(input("Enter your car year: "))
color = input("Enter your car color: ")
num_cupholders = input("Enter your car number of cupholders: ")

# Create an instance of the `Car` class and pass in the variables from the user.
car = Car(make, model, body, engine, year, color, num_cupholders)

# Print the details of the car
print('Here is the information you enter for the car.')
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Body: {car.body}")
print(f"Engine: {car.engine}")
print(f"Year: {car.year}")
print(f"Color: {car.color}")
print(f"Number Cupholders: {car.num_cupholders}")