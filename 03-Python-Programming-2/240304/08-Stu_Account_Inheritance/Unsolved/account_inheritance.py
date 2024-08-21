# Import the SavingsAccount and CD classes from the Accounts.py file.
# ADD YOUR CODE HERE
from Accounts import SavingsAccount, CD

# import Accounts
# account = Accounts.SavingsAccount()

# Prompt the user to set the savings balance and interest rate.
savings_balance = float(input("What is your balance? "))
interest_rate = float(input("What is the Interest Rate for the Savings Account? "))

# Create an instance of the `SavingsAccount` class that sets the users savings account balance and interest.
# ADD YOUR CODE HERE
savings_data = SavingsAccount(savings_balance, interest_rate)

# Prompt the user to set the CD balance, interest rate, and months for the CD.
cd_balance = float(input("What is your CD balance? "))
cd_interest_rate = float(input("What is the Interest Rate for the CD? "))
cd_months = int(input("How many months is the CD? "))

# Create an instance of the `CD` class that sets the users cd account balance, interest, and length of months.
# ADD YOUR CODE HERE
cd_data = CD(cd_balance, cd_interest_rate, cd_months)

# Display the savings account data.
print('Here are the details of the savings account.')
print("The balance is: $", format(savings_data.get_balance(), ',.2f'))
print("APR Interest Rate is: ", format(savings_data.get_interest(), ',.2f'),"%")

# Display the CD account data.
print('Here are the details of the CD account.')
print("The balance is: $", format(cd_data.get_balance(), ',.2f'))
print("APR Interest Rate is:", format(cd_data.get_interest(), ',.2f'),'%')
print(f"Length of CD is: {cd_data.get_months()} months.")
