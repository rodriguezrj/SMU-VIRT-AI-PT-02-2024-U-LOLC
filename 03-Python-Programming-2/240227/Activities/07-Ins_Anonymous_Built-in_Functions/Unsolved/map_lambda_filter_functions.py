# # Anonymous Functions

# # 1. A function that divides by 7 and rounds to the nearest hundredth
# def divide_by_seven(num):
#     return round(num / 7, 2)

# num = [24, 654, 3, 961, 21]

# full_contents = []
# for x in num:
#     full_contents.append(divide_by_seven(x))

# print(full_contents)
# print()
# print("*" * 60)

# list_comp = [divide_by_seven(x) for x in [24, 654, 3, 961, 21]]
# print(list_comp)
# print("*" * 60)
# print()

# list_comp = [divide_by_seven(x) for x in num]
# print(list_comp)
# print("*" * 60)
# print()

# map_function = list(map(divide_by_seven, (24, 654, 3, 961, 21)))
# print(map_function)
# print("*" * 60)
# print()

# map_function = list(map(divide_by_seven, num))
# print(map_function)
# print("*" * 60)
# print()

# # 4. Demonstrate how to implement the previous example as a lambda function within the map function
# map_function = list(map(lambda x: round(x / 7, 2), (24, 654, 3, 961, 21)))
# print("MAP FUNCTION")
# print(map_function)
# print()


# 5. Use the filter and lambda functions to get only the numbers divided by 3.
numbers = [12, 7, 9, 18, 25, 36, 42, 55, 63]

divisible_by_3 = []
for x in numbers:
    if x%3 == 0:
        divisible_by_3.append(x)
print(divisible_by_3)

## Regular List comprehension
divisible_by_3 = [x for x in numbers if x%3==0]
print(divisible_by_3)

## Filter
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(divisible_by_3)

# divisible_by_3 = filter(lambda x: x % 3 == 0, numbers)
# print(divisible_by_3)










