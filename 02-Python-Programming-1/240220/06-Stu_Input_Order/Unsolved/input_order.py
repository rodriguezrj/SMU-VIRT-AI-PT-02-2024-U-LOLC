# Take input of an item the user wants to purchase
purchase = input("what is your item? ")

# Ask how much the item costs and cast it as a number.
# What type of number should it be cast as?
item_cost = float(input("how much is the item? "))


# Ask what quantity of the item should be purchased and cast it as a number.
# What type of number should it be cast as?
quantity = int(input("how many items do you want? "))

# Print the item cost along with its data type
print("My item cost is " + str(item_cost) + " and the type is " + str(type(item_cost)))
print("My item cost is", item_cost, "and the type is", type(item_cost))

# Print the item quantity along with its data type
print("My item quantity is " + str(quantity) + " and the type is " + str(type(quantity)))


# Print results
