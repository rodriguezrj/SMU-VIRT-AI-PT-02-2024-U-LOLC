# Ask the user what their vacation budget is and convert it to a float
budget = float(input("What is your total vacation budget? "))
# budget = 10101.10

# Ask the user how much of their budget should be spent on flights and 
# accommodation and convert it to a float
flights_accommodation = float(input("What is your budget for the flights and "
                                    + "accommodation? "))

# Ask the user how much they would like to spend per day and convert it to a float
daily_budget = float(input("What is your preferred daily budget? "))

# Ask the user how many days they will go on vacation and convert it to an
# integer
vacation_days = float(input("How many days will you go on vacation? "))

# Ask the user the currency exchange rate for the country they're visiting and
# convert it to a float
exchange_rate = float(input("What is the currency exchange rate? "))

# Ask the user for the radius distance they're willing to walk from their
# hotel and convert it to a float
distance = float(input("What is the radius distance you're willing to walk "
                       + "from your hotel (in meters)? "))

# Calculate the budget remaining after flights and accommodation
remaining_budget = budget - flights_accommodation
print("remaining budget:", budget - flights_accommodation)
print("remaining budget:", remaining_budget)

# Calculate the remaining budget in local currency amount
# budget_local_cur = (budget - flights_accommodation) * exchange_rate
budget_local_cur = remaining_budget * exchange_rate
print("remaining budget in local currency:", budget_local_cur)

# Calculate the budget per day in the local currency
budget_per_day = budget_local_cur / vacation_days
print("remaining budget per day:", round(budget_per_day, 2))

# Calculate the budget per day in the local currency, ignoring cents
# this overwrites the previous budget_per_day variable
budget_per_day = budget_local_cur // vacation_days
print("remaining budget per day without cents:", budget_per_day)

# Calculate the total area around the hotel the user can walk within
# Area of a circle = pi * radius ** 2
pi = 3.14159265358979323846
area = pi * distance ** 2
print("walking distance in m^2:", area)

# Calculate the amount left from the budget if the user sticks with their
# daily budget. This is a modulus problem.
remainder = remaining_budget % (daily_budget * vacation_days)
print("Budget remaining if the daily goal is met:", remainder) 
