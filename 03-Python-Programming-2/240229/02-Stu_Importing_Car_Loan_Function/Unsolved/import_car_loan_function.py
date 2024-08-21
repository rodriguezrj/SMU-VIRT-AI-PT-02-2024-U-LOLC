# Import the calculate_future_value function from the CarLoan file.
from CarLoan import calculate_future_value
import CarLoan
# CarLoan.calculate_future_value()

# Create the new_car_loan dictionary.
new_car_loan = {
    "current_loan_value": 25000,
    "months_remaining": 12,
    "annual_interest_rate": 0.0315
    }

# Set the function call equal to a variable called car_value.
# Pass the relevant information from the dictionary as parameters to the function call.
# (current_loan_value, annual_interest_rate, months_remaining)
current_car_value = calculate_future_value(**new_car_loan)
print(f"${current_car_value:.2f}")
print("$", round(current_car_value, 2))

current_car_value = calculate_future_value(new_car_loan['current_loan_value'], new_car_loan['annual_interest_rate'], new_car_loan['months_remaining'])
print(f"${current_car_value:.2f}")
print("$", round(current_car_value, 2))
print("$" + f"{round(current_car_value, 2)}")


# Print the future value of the car to 2 decimal places.
# print(f"{current_car_value:.2f}")
# print(round(current_car_value, 2))
