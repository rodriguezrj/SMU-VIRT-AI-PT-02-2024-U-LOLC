"""Pizza Order"""

def create_pizza_order():
    '''
    Definition:
        This function asks for customer order with 3 toppings and then returns them to the customer

    Args:
        None

    Raises:
        ErrorType: If the user enters a number less than 1 or greater than 5
        then asks the user to try again.
        
    Returns:
        selected_toppings (List): this is a list of the 3 items the customer selected
    Notes:
        None
    '''
    toppings = ['pepperoni', 'mushrooms', 'onions', 'sausage', 'bell peppers']

    print("Welcome to the Sal's Famous Pizza!")
    print("Please choose three toppings for your pizza from the following options:")

    for i, topping in enumerate(toppings, start=1):
        print(f"{i}. {topping}")

    selected_toppings = []
    for _ in range(3):
        topping_number = int(input("Enter the number of your chosen topping: "))
        while topping_number < 1 or topping_number > 5:
            print("Invalid topping number. Please try again.")
            topping_number = int(input("Enter the number of your chosen topping: "))

        selected_toppings.append(toppings[topping_number - 1])

    print("Here is your order:")
    print("Your pizza comes with:", ", ".join(selected_toppings))

    # return selected_toppings

if __name__ == "__main__":
    create_pizza_order()
    # selected_toppings = create_pizza_order()
    # print(selected_toppings)
