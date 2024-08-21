"""This is a basic ATM Application.
This is a program consists of the basic actions of an ATM.
"""

accounts = [
    {
    "pin": 123456,
    "balance" : 1436.19},
    {
    "pin" : 246802,
    "balance": 3571.87},
    {
    "pin": 135791,
    "balance" : 543.79},
    {
    "pin" : 123987,
    "balance": 25.89},
    {
    "pin" : 269731,
    "balance": 3278.42}
]

# Define the `login` function for the ATM application.
def login(pin):
    """The function a for loop to check to validate the PIN against this list of `accounts`.
        If the PIN is validated, the function should return the account's balance.
    Args:
        pin (integer): The users pin number

    Returns:
        If the pin matches one of the pin numbers in the "accounts"
        the account balance is returned.
    """
    for account in accounts:
        if int(pin) == account["pin"]:
            account_balance = account['balance']

    return account_balance


# Define the `check_balance` function for the ATM application.
def check_balance(account_balance:float):
    """The function uses the account balance as a parameter.
    and returns the balance of the account.

    Args:
        account_balance (float): The balance of the account.

    Returns:
        Prints the account balance formatted to two decimal places and thousandths.
    """
    print(f"the balance in your account is ${round(account_balance, 2)}.")


# Define the `make_deposit` function for the ATM application.
def make_deposit(account_balance, deposit):
    """This function takes in the account balance and deposit amount as parameters.
    Initializes deposit balance equal to the account balance.
    Then validates that the deposit amount is greater than 0.

    Args:
        account_balance (float): The balance of the account
        deposit (float): An amount deposited into the account greater than 0.

    Returns:
        The function returns the balance after being adjusted for the deposit.

    Notes:
        The deposit balance should equal the account balance plus the deposit amount.
    """
    if deposit > 0:
        deposit_balance = account_balance + deposit
    else:
        print("Your deposit amount must be positive")
    return deposit_balance


# Define the `make_withdrawal` function for the ATM application.
def make_withdrawal(account_balance, withdrawal):
    """This function should take in the account balance and withdrawal amount as parameters.
    The function validates that the account balance is greater than the withdrawal.

    Args:
        account_balance (float): The balance of the account.
        withdrawal (integer): Withdrawals are whole dollars.

    Returns:
         The function returns the account balance after being adjusted for the withdrawal.

    Notes:
        The withdrawal balance should equal the account balance minus the withdrawal amount.
    """
    if account_balance < withdrawal:
        print("You do not have the funds to make this withdrawal.")
    else:
        withdrawal_balance = account_balance - withdrawal

    # if account_balance > withdrawal:
    #     withdrawal_balance = account_balance - withdrawal
    # else:
    #     print("You do not have the funds to make this withdrawal.")


    return withdrawal_balance

