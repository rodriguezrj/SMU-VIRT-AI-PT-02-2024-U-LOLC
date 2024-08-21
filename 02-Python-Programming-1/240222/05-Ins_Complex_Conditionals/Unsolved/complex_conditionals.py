# Declare variables
x = 1
y = 10

# Logical operators: "and" and "or"

# Check for two conditions to be met using "and"
if x == 1 and y == 10:
    print("both values returne true")


# Check if either of two conditions is met using "or"
if x < 45 or y < 5:
    print("one or more statements are true")

# Check if a condition is not true
if not(x > y):
    print("x is not greater than y")

# Check multiple conditions
plate = "fancy"
if plate == "cracked":
    print("Throw the dish away")
elif plate == "fancy":
    print("Put the plate on the top shelf")
else:
    print("Put the plate on the bottom shelf")


# Conditionals with membership operators: "in" and "not in"

# Check if a variable is in a list
name = "Amidah"
group_one = ["Jorge", "Joon", "Susan"]
group_two = ["Gerald", "Paola", "Ryder"]
group_three = ["Farah", "Amidah", "Koen"]

if name in group_one:
    print("group 1")
elif name in group_two:
    print("group 2")
elif name in group_three:
    print("group 3")
else:
    print('''it's not in any''')


# Check if a variable is not in a list
countries = ["Fiji", "Australia", "New Zealand", "Papua New Guinea", "Palau"
             "Solomon Islands", "Micronesia", "Vanuatu", "Samoa", "Kiribati",
             "Tonga", "Marshall Islands", "Tuvalu", "Nauru"]
country = "Kenya"

if country not in countries:
    print("country not here")

# Conditionals with identity operators: "is" and "is not"

# Check if a variable is a list
if type(countries) is list:
    print("countries is a list")
elif type(countries) is not list:
    print("country is not a list")

# Check if a variable is not a list
x = 100.00
if type(x) is float:
    print("x is a float")
elif type(x) is int:
    print("x is an int")


# Check if a variable is a float or integer


# Check multiple conditions with comparison and logical operators
height = 66
age = 16
adult_permission = True

if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("Can ride bumper cars")
else:
    print("Stick to lazy river")
