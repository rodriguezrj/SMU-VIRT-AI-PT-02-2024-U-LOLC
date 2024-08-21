# Declare variables
x = 1
y = 10

# Check if one value is equal to another
if x == 1:
    print(x)


# Check if one value is NOT equal to another
if x != 1:
    print(x)


# Check if one value is less than another
if x < y:
    print("x is less than y")


# Check if one value is greater than another
if y > x:
    print("y is greater than x")

if x > y:
    print("y is greater than x")


# Check if a value is greater than or equal to another
if x >= 1:
    print("x is greater than or equal to 1")

# Use a Boolean to check a condition
congratulations = True

if congratulations:
    print("Congratulations")
elif x == 2:
    print("Awesome")
else:
    print("How are you feeling")


if congratulations:
    print("Congratulations")
else:
    print("How are you feeling")

if congratulations:
    print("Congratulations")
else:
    print("Awesome")



if dishes_broken:
    print("throw away")
elif dish_plain:
    print("put in the pantry")
elif dish_fancy:
    print("put in the fancy pantry")
else:
    print("put all in the cupboard")


# Get an input from a user

# Check if the user input is a number
altitude = "66,000"
altitude = "66000"

if altitude.isdigit():
    print(f"The plane flew at {altitude} feet")
else:
    print(f"{altitude} cannot be converted to a number")