# Boolean to place the order
place_order = True

# List to track pie purchases
pie_purchases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Pie List
pie_list = ["Pecan", 
            "Apple", 
            "Lemon Meringue", 
            "Banoffee", 
            "Black Bun",
            "Bean", 
            "Buko", 
            "Burek", 
            "Tamale", 
            "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while place_order:

    # Show pie selection prompt
    print("-" * 50) #--------------------------------------------------#
    pie_number = 1
    for pie in pie_list:
        print(f"({pie_number}) {pie}")
        pie_number += 1 # pie_number = 2

    pie_choice = input("Which would you like? ")

    # Get index of the pie from the selected number
    choice_index = int(pie_choice) - 1

    # Add pie to the pie list by finding the matching index and adding one to its value
    pie_purchases[choice_index] += 1

    print("-" * 50)

    # Inform the customer of the pie purchase
    print("Great! We'll have that " + pie_list[choice_index] 
          + " Pie right out for you.")

    # Provide exit option
    while True:
		# Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # Check the customer's input
        match keep_ordering.lower():
            # Customer chose yes
            case 'y':
                # Keep ordering
                place_order = True
                # Exit the keep ordering question loop
                break

            # Customer chose no
            case 'n':
                # Complete the order
                place_order = False

                # Since the customer decided to stop ordering, thank them for their order
                print('thank you')

                # Exit the keep ordering question loop
                break

            # Customer typed an invalid input
            case _:
                print("I don\'t understand")
                # Tell the customer to try again

    # while True:
	# 	# Ask the customer if they would like to order anything else
    #     keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

    #     # Check the customer's input
    #     if keep_ordering.lower() == 'y':
    #             # Keep ordering
    #             place_order = True

    #             # Exit the keep ordering question loop
    #             break
    #         # Customer chose no
    #     elif keep_ordering.lower() == 'n':
    #             # Complete the order
    #             place_order = False

    #             # Since the customer decided to stop ordering, thank them for their order
    #             print("tahnk you")
    #             # Exit the keep ordering question loop
    #             break

    #         # Customer typed an invalid input
    #     else:
    #          print("I don\'t udnerstand. please try again.")
    #             # Tell the customer to try again



# Once the pie list is complete
print("-" * 50)

# Count instances of each pie
print("You purchased: ")

# Loop through the full pie list
for pie_index in range(len(pie_list)):
    pie_count = pie_purchases[pie_index] # [0, 0, 2, 0, 1, 0, 0, 0]
    pie_name = pie_list[pie_index] # [pecan, etc.]

    # If the pie count is greater than or equal to 1:
    if pie_count >= 1:
        # Gather the count of each pie in the pie list and print them alongside the pies
        print(f"{pie_count} {pie_name} Pie")
