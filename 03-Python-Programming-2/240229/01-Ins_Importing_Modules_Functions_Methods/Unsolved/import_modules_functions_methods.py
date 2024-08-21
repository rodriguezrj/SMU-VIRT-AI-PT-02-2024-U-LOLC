"""Importing  modules, functions and methods"""

# Import the sqrt function from the math module.
from math import sqrt

# Calculate the square root of a number.
number = 16
result = sqrt(number)
print(result)

# Import the randint and choice methods from the random module.
# import random
# random.randint()
from random import randint, choice

# Generate a random number between 1 and 10 and selecting a random element from a list.
random_number = randint(1, 10)
print(random_number)

# Use the choice method to randomly select an element from the list.
my_list = ['apple', 'banana', 'orange', 'grape', 'mango']
random_choice = choice(my_list)

print(random_choice)

# Import the datetime and date classes from the datetime module.
from datetime import datetime, date

# Get the current datetime using the now function.
current_datetime = datetime.now()

current_time = current_datetime.strftime("%H:%M:%S")

current_date = date.today()

print(current_datetime)
print(current_time)
print(current_date)